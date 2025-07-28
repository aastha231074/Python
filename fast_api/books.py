from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'title one', 'author': 'author one', 'category': 'science'},
    {'title': 'title two', 'author': 'author two', 'category': 'science'},
    {'title': 'title three', 'author': 'author three', 'category': 'history'},
    {'title': 'title four', 'author': 'author four', 'category': 'maths'},
    {'title': 'title five', 'author': 'author five', 'category': 'english'},
    {'title': 'title six', 'author': 'author two', 'category': 'maths'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def read_category_by_query(category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)