from sqlalchemy import Column, Integer, String, relationship
from sqlalchemy.ext.declarative import declarative_base

from .ocean import Ocean
from .rock import Rock

Base = declarative_base()

class River(Base):
    __tablename__ = 'rivers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    oceans = relationship(Ocean, secondary="river_ocean", backref="rivers")
    rocks = relationship(Rock, secondary="river_rock", backref="rivers")

class RiverOcean(Base):
    __tablename__ = "river_ocean"

    river_id = Column(Integer, ForeignKey("rivers.id"), primary_key=True)
    ocean_id = Column(Integer, ForeignKey("oceans.id"), primary_key=True)
