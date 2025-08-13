# --------TO RUN--------
# uvicorn books_2:app --reload -> click on the links -> change the url = {url}/docs (for swagger UI)
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal

app = FastAPI()

# ---------------------------------------------------
# models.Base -> This refers to a declarative base class that's typically created with declarative_base() from SQLAlchemy
# metadata -> This is an attribute of the base class that contains information about all the tables defined in your model -their schema, columns etc
# create_all -> This method creates all the tables defined in your models in the database if they don't exist
# bind=engine -> This specifies which database engine to use. The engine is a SQLAlchemy Engine object that represents the connection to your specific database 
# ---------------------------------------------------
models.Base.metadata.create_all(bind=engine)

# Before each request we are able to fetch the DB session local, 
# i.e. open up connection and close a connection on every request sent to the fastAPI application 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/",  status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')