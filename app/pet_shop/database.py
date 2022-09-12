from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = 'sqlite:///./shop.db'

engine = create_engine(SQL_URL, connect_args = {"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
        conn = engine.connect()
        conn.close()
    finally:
        db.close()

Base = declarative_base()

