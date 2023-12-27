from psycopg2.extras import RealDictCursor
from ..models.book import Book
from ..db_create import Database

class BookRepository:

    def __init__(self):
        self.connection = Database.connection
       

    def get_all_books(self):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
        return books

    def create_book(self, book:Book):   
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                INSERT INTO books (id,title,status) VALUES (%s,%s,%s) RETURNING id;
                """, (book.id,book.title,book.status)
            )
            book_id = cursor.fetchone()["id"]
            self.connection.commit()
        return book_id

    def get_book(self, book_id):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT * FROM books WHERE id = %s", (book_id,)
            )
            book = cursor.fetchone()
        return book
    
    def update_book_status(self, book_id, new_status):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "UPDATE books SET status = %s WHERE id = %s", (new_status, book_id)
            )
            self.connection.commit()
    

    def delete_book(self, book_id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM books WHERE id = %s", (book_id,)
            )
            self.connection.commit()
