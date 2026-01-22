from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time

DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_NAME = os.getenv("POSTGRES_DB", "db")
DB_HOST = os.getenv("DB_HOST", "localhost")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

app = FastAPI()

Base = declarative_base()

class Visit(Base):
    __tablename__ = "visits"
    id = Column(Integer, primary_key=True, index=True)
    visitor_name = Column(String, index=True)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            engine = create_engine(DATABASE_URL)
            Base.metadata.create_all(bind=engine)
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            return SessionLocal()
        except Exception as e:
            print(f"Baza jeszcze śpi... czekamy. Błąd: {e}")
            time.sleep(5)
            retries -= 1
    raise Exception("Nie udało się połączyć z bazą danych")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    db = get_db_connection()
    new_visit = Visit(visitor_name="keepitfoxy")
    db.add(new_visit)
    db.commit()
    
    count = db.query(Visit).count()
    version = os.getenv("APP_VERSION", "default")
    
    return {
        "message": "Hello keepitfoxy!",
        "version": version,
        "db_status": "Connected",
        "total_visits": count
    }
