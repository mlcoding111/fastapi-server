from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from ..db import Base

class BaseModel(Base):
    """
    Base model class that provides common fields for all models.
    All models should inherit from this class to get default fields.
    """
    __abstract__ = True  # This tells SQLAlchemy not to create a table for this class
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)