from ..models.book import Book, BookCreateDto
from ..repositories.book_repository import BookRepository
from fastapi import APIRouter,Depends, status
from fastapi.responses import JSONResponse
from uuid import uuid4
router = APIRouter()

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    responses={
        404: {"description": "Not Found"},
        422: {"description": "Validation Error"},
    },
)

@router.get("/", summary="Get All Books", description="Returns a list of all books")
async def get_all_books(repository: BookRepository = Depends()):
    books =  repository.get_all_books()
    return books

@router.post("/", summary="Create a Book", tags=["Books"], description="Creates a new book", status_code=status.HTTP_201_CREATED)
async def create_book(book:BookCreateDto,repository: BookRepository = Depends()):
    book = Book(uuid4().__str__(),book.title,"to-read")
    book_id = repository.create_book(book)
    return JSONResponse({"message": "Book created successfully", "id": book_id}, status_code=status.HTTP_201_CREATED)

@router.get("/{book_id}", summary="Get a Specific Book", tags=["Books"], description="Get details of a specific book by its ID")
async def get_book(book_id: str,repository:BookRepository = Depends()):
    book = repository.get_book(book_id)
    if book:
        return book
    else:
        return JSONResponse({"message": "Book not found"}, status_code=status.HTTP_404_NOT_FOUND)
    
@router.put("/{book_id}", summary="Update Status of Book", tags=["Books"], description="Update status of a specific book by its ID")
async def get_book(book_id: str,book_status:str,repository:BookRepository = Depends()):
    repository.update_book_status(book_id,book_status)
    return JSONResponse({"message": "Book status changed successfully"}, status_code=status.HTTP_200_OK)
        

@router.delete("/{book_id}", summary="Delete a Book", tags=["Books"], description="Deletes a book by its ID")
async def delete_book(book_id: str, repository:BookRepository = Depends()):
    repository.delete_book(book_id)
    return JSONResponse({"message": "Book deleted successfully"}, status_code=status.HTTP_200_OK)
