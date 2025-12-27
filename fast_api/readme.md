# What is FastAPI? 
<b> FastAPI </b> is a Python web-framework for building modern APIs. FastAPI is built on Starlette ( for web handling ) and Pydantic ( for data validation )
Automatically generates:
- Swagger UI (/docs)
- ReDoc (/redoc)

## HTTP Request 
An HTTP request is the fundamental method of communication on the World Wide Web, using the Hypertext Transfer Protocol. When you visit a website, your browser sends HTTP requests to the server to get the necessary data (HTML pages, images, etc.). 
### Key characteristics of an HTTP request:
- Protocol: It strictly adheres to the rules defined by the HTTP standard.
- Structure: Every HTTP request message has a specific format, including:
    1. A Request Line: Specifies the HTTP method (e.g., GET, POST, PUT, DELETE), the target Uniform Resource Identifier (URI), and the HTTP version.
    2. Headers: Provide metadata about the request, such as the user agent, accepted formats, or host information.
    3. An optional Body: Contains data being sent to the server (e.g., form data when logging in or submitting information).
    4. Stateless: Each HTTP request is treated as an independent transaction; the server does not retain knowledge of past requests (unless handled by the application logic, e.g., using cookies). 

## How to use FastAPI 
### Import FastAPI: 
```python 
from fastapi import FastAPI

app = FastAPI()
```

### Run FastAPI application: 
```ssh
uvicorn python-file:app --reload
```

```ssh
fastapi run python-file.py 
```

```ssh
fastapi dev python-file.py 
```

### Create endpoints: 
#### GET method: 
```python 
@app.get("/api-endpoint")
async def first_api():
    return {'message' : 'Hello Aastha!'}
```

#### Path Parameters:
- Path parameters are request parameters that have been attached to the URL. 
- Path parameters are usually defined as a way to find information based on location

```python 
@app.get("/api-endpoint/{dynamic_param}")
async def first_api(dynamic_param):
    return {'dynamic_param' : dynamic_param}
```

##### Order matter with path parameter: 
e.g. REQUEST: 127.0.0.1:8000/books/my_books

```python 
@app.get("/api-endpoint/{dynamic_param}")
async def first_api(dynamic_param):
    return {'dynamic_param' : dynamic_param}

@app.get("/api-endpoint/my_books")
async def first_api(dynamic_param):
    return {'book title' : 'My favorite book'}

```

What happens is my_books get transformed into the dynamic param of our first function. So our second function never gets called because the first function is accepting the exact same parameter list. 

###### What we need to do? 
Revers the order

```python 
@app.get("/api-endpoint/my_books")
async def first_api():
    return {'book title' : 'My favorite book'}

@app.get("/api-endpoint/{dynamic_param}")
async def first_api(dynamic_param : type):
    return {'dynamic_param' : dynamic_param}
```

In an api url you can not have spaces 
REQUEST: URL: 127.0.0.1:8000/books/title%20four = title four 

#### Query Parameters:
- Query Parameters are request parameters that have been attached after a "?"
- Query Parameters have a name-value pairs
    example: 127.0.0.1:8000/?category=math

```python 
@app.get("/books/")
async def read_category_by_query(category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return 
```

#### POST method: 
- Usd to create data 
- POST can have a body that has additional information that GET does not have 

```python 
from fastapi import Body, FastAPI

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
```

#### PUT method: 
- Used to update data 
- PUT can have a body that has additional information ( like POST ) that GET does not 

```python 
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
```

#### DELETE method: 
- Used to delete data 

```python 
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
```

