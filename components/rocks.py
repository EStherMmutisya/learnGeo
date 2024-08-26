from sqlalchemy import Column, Integer, String, ForeignKey, relationship

from sqlalchemy.ext.declarative import declarative_base

from .ocean import Ocean  # Import the Ocean model
from .river import River  # Import the River model (assuming it exists)

Base = declarative_base()

class Rock(Base):
    __tablename__ = 'rocks'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    