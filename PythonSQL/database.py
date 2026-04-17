import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import urllib.parse

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = urllib.parse.quote_plus(os.getenv("DB_PASSWORD", "Incedo@123"))
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydatabase")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # base model for our models