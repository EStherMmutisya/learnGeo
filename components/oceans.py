from sqlalchemy import Column, Integer, String, relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ocean(Base):
    __tablename__ = 'oceans'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    rivers = relationship("River", secondary=lambda: RiverOcean.__table__)