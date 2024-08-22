from sqlalchemy import Column, Integer, String, ForeignKey, relationship

from sqlalchemy.ext.declarative import declarative_base

from .ocean import Ocean  # Import the Ocean model

Base = declarative_base()

class Rock(Base):
    __tablename__ = 'rocks'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    ocean_id = Column(Integer, ForeignKey('oceans.id'))
    ocean = relationship("Ocean", backref="rocks")

    rivers = relationship("River", secondary=lambda: RiverRock.__table__)