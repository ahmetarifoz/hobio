from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from core.db import Base

class Hobby(Base):
    __tablename__ = "hobbies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # İlişkiler
    users = relationship("UserHobby", back_populates="hobby")
    lobbies = relationship("Lobby", back_populates="hobby")

class UserHobby(Base):
    __tablename__ = "user_hobbies"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    hobby_id = Column(Integer, ForeignKey("hobbies.id"), nullable=False)
    proficiency = Column(String(50), nullable=False)

    user = relationship("User", back_populates="hobbies")
    hobby = relationship("Hobby", back_populates="users")
