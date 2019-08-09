import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

class Config(object):
    engine = create_engine(
    "mysql+mysqlconnector://root:vitrygtr@localhost:3306/seqbox",
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)

DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"
# Secret key for signing cookies
SECRET_KEY = "secret"
 
