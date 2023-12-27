from pydantic import BaseModel
from dataclasses import dataclass
from uuid import uuid4 

    

@dataclass
class Book:
    id:str
    title:str
    status:str


class BookCreateDto(BaseModel):
    title:str


