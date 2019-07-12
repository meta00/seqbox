
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine 
 
engine = create_engine(
    "mysql+mysqlconnector://root:vitrygtr@localhost:3306/seqbox",
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)
 
engine.connect()
 
print(engine)