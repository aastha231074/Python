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
async def first_api(dynamic_param):
    return {'book title' : 'My favorite book'}

@app.get("/api-endpoint/{dynamic_param}")
async def first_api(dynamic_param):
    return {'dynamic_param' : dynamic_param}
```

In an api url you can not have spaces 
REQUEST: URL: 127.0.0.1:8000/books/title%20four = title four 