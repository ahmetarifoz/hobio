
from fastapi import FastAPI
from core.auth_router import router as auth_router
from core.db import SessionLocal
from helpers.auth_helpers import create_admin_user
from sqlalchemy.orm import Session
app = FastAPI(title="FastAPI", version="0.0.1")

@app.on_event("startup")
def startup_event():
    db: Session = SessionLocal()
    try:
        create_admin_user(db)  # Admin kullanıcı oluşturma işlemi
    finally:
        db.close()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])