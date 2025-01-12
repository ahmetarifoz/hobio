from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func, Enum
from sqlalchemy.orm import relationship
from core.db import Base
import enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    USER = "user"
    MODERATOR = "moderator"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)  

    hobbies = relationship("UserHobby", back_populates="user")
    tags = relationship("UserTag", back_populates="user")
    lobbies = relationship("UserLobby", back_populates="user")
    messages = relationship("Message", back_populates="user")
    events = relationship("UserEvent", back_populates="user")