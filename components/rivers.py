from sqlalchemy import Column, Integer, String, relationship

from sqlalchemy.ext.declarative import declarative_base

from .ocean import Ocean
from .rock import Rock

Base = declarative_base()

class River(Base):
    __tablename__ = 'rivers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    oceans = relationship(Ocean, secondary=lambda: RiverOcean.__table__, backref="rivers")
    rocks = relationship(Rock, secondary=lambda: RiverRock.__table__, backref="rivers")