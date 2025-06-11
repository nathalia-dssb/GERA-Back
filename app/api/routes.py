from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from sqlalchemy import text

router = APIRouter()

@router.get("/health", tags=["Test"])
def health_check():
    return {"status": "ok", "message": "API is working"}

@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Database connection successful"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}