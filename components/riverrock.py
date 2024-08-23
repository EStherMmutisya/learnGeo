from sqlalchemy import Column, Integer, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RiverRock(Base):
    __tablename__ = 'river_rocks'

    river_id = Column(Integer, ForeignKey('rivers.id'), primary_key=True)
    rock_id = Column(Integer, ForeignKey('rocks.id'), primary_key=True)