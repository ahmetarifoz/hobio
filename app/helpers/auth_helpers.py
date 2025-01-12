from sqlalchemy.orm import Session
from domains.users.models import User, UserRole
from passlib.context import CryptContext

# Şifreleme için Passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_admin_user(db: Session):

    admin_username = "admin"
    admin_password = "123456"
    admin_email = "admin@admin.com"

    admin_user = db.query(User).filter(User.username == admin_username).first()
    if not admin_user:
        new_admin = User(
            username=admin_username,
            email= admin_email,
            hashed_password=get_password_hash(admin_password),
            role=UserRole.ADMIN
        )
        db.add(new_admin)
        db.commit()
        print(f"Admin kullanıcı oluşturuldu: {admin_username}")
    else:
        print("Admin kullanıcı zaten mevcut.")
