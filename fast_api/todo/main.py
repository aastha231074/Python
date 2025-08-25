# --------TO RUN--------
# uvicorn main:app --reload -> click on the links -> change the url = {url}/docs (for swagger UI)
from fastapi import FastAPI

import models
from database import engine
from router import auth, todos

app = FastAPI()

# ---------------------------------------------------
# models.Base -> This refers to a declarative base class that's typically created with declarative_base() from SQLAlchemy
# metadata -> This is an attribute of the base class that contains information about all the tables defined in your model -their schema, columns etc
# create_all -> This method creates all the tables defined in your models in the database if they don't exist
# bind=engine -> This specifies which database engine to use. The engine is a SQLAlchemy Engine object that represents the connection to your specific database 
# ---------------------------------------------------
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)