from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HealthFacility(Base):
    __tablename__ = "health"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    staff = Column(Integer)