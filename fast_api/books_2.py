# --------TO RUN--------
# uvicorn books_2:app --reload -> click on the links -> change the url = {url}/docs (for swagger UI)
from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description 
        self.rating = rating 

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