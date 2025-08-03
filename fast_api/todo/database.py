from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False} # By default SQLite allow only one thread to communicate with it 
    # -----------------------------------------------------
    # This line sets up a connection to an SQLite database,
    # allowing it to be safely shared across different threads.
    # -----------------------------------------------------
)

# A new database session
SessionLocal = sessionmaker(
    autoflush=False, # prevents automatic flushing of changes to the database before a query is run 
    autocommit=False, # explicitly call commit() to save changes to the database 
    bind=engine # this tells the session what database it should connect to 
)

# create a base which is an object of the database 
Base = declarative_base()

