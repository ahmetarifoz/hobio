from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.db import SessionLocal
from core.auth_service import verify_password, create_access_token, get_current_user,register_user
from domains.users.models import User, UserRole

router = APIRouter()

# Veritabanı bağlantısı
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Kullanıcı Girişi - Token Alma


@router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Kullanıcı adı zaten alınmış")
    register_user(db, username, email, password)
    return {"message": "Kullanıcı kaydı başarılı"}

@router.post("/logout")
def logout(current_user: User = Depends(get_current_user)):
    
    return {"message": "Çıkış başarılı"}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.username, "role": user.role.value})
    return {"access_token": access_token, "token_type": "bearer"}

# Mevcut Kullanıcı Bilgisi
@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role.value,
        "bio": current_user.bio,
        "created_at": current_user.created_at
    }

# Kullanıcı Role Tabanlı Erişim
@router.get("/admin-only")
def admin_only_route(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Access forbidden: Admins only")
    return {"message": f"Welcome, {current_user.username}. You are an admin!"}
