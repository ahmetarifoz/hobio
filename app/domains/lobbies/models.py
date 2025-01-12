from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from core.db import Base
class Lobby(Base):
    __tablename__ = "lobbies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    hobby_id = Column(Integer, ForeignKey("hobbies.id"), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # İlişkiler
    hobby = relationship("Hobby", back_populates="lobbies")
    members = relationship("UserLobby", back_populates="lobby")
    messages = relationship("Message", back_populates="lobby")
    events = relationship("Event", back_populates="lobby")

class UserLobby(Base):
    __tablename__ = "user_lobbies"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lobby_id = Column(Integer, ForeignKey("lobbies.id"), nullable=False)
    joined_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="lobbies")
    lobby = relationship("Lobby", back_populates="members")
