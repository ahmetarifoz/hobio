from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from core.db import Base
class UserTag(Base):
    __tablename__ = "user_tags"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tag = Column(String(50), nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="tags")
