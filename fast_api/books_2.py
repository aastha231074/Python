# --------TO RUN--------
# uvicorn books_2:app --reload -> click on the links -> change the url = {url}/docs (for swagger UI)
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description 
        self.rating = rating 

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1, max_length = 100)
    rating: int = Field(gt = 0, lt = 5)

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithaastha', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithaastha', 'This is a great book!', 5),
    Book(3, 'Master End Point', 'codingwithaastha', 'This is an awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description!', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description!', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description!', 1)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

# Without data validation 
# @app.post("/create-book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)

# With data validation 
@app.post("/create-book")
async def create_book(book_request: BookRequest):
    # dict is deprecated 
    # new_book = Book(**book_request.dict())
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)