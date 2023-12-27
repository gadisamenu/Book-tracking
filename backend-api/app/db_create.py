from psycopg2 import connect, extensions, sql
import os
from .config import *

class Database:
    connection = None

    @staticmethod
    def connect():
        # Try connecting to the database
        connection = None
        try:
            connection = connect(
                host=postgres_host,
                dbname=postgres_db,
                user=postgres_user,
                password=postgres_password,
            )
            print("Connected to existing database")
        except Exception as e:
            # Database connection failed, check if database exists
            if e.__class__.__name__ == "OperationalError":
                print("Database connection failed, checking if database exists...")
                connection = connect(
                    host=postgres_host,
                    user=postgres_user,
                    password=postgres_password,
                )
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{os.getenv('POSTGRES_DB')}'")
                    exists = cursor.fetchone()

                if not exists:
                    print("Database does not exist, creating...")
                    cursor.execute(f"CREATE DATABASE {os.getenv('POSTGRES_DB')}")
                    connection.commit()
                    print("Database created successfully")
                else:
                    print("Database exists but connection failed, retrying...")
                    connection.close()
                    connection = connect(
                        host=postgres_host,
                        dbname=postgres_db,
                        user=postgres_user,
                        password=postgres_password,
                    )
                  
                    print("Connected to database")
            else:
                raise e
        finally:
            if connection != None:
                # set isolation level and create cursor
                connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
                cursor = connection.cursor()

                # assign connection to class attribute
                Database.connection = connection
                Database.__create_table_if_not_exists__()


        

    @staticmethod
    def __create_table_if_not_exists__():
        # Check if connection exists
        if not Database.connection:
            raise Exception("Database connection not established")
        talbes_query = [
            "CREATE TABLE IF NOT EXISTS books (id VARCHAR(255) PRIMARY KEY, title VARCHAR(255) NOT NULL, status VARCHAR(255) NOT NULL);"
        ]
        
        for table_query in talbes_query:
            cursor = Database.connection.cursor()
            cursor.execute(table_query)
            Database.connection.commit()
        
    @staticmethod
    def close():
        if Database.connection != None: 
            Database.connection.close()