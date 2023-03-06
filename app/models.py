from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from app.database import Base

class Opening(Base):
    __tablename__ = "openings"
    id = Column(Integer, primary_key=True, index=True)
    moves = Column(String)
    name = Column(String(255))
    ecocode = Column(String(10))
    description = Column(String)

