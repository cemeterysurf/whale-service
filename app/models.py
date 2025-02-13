from sqlalchemy import Column, Float, String, Integer
from .database import Base


class Whale(Base):
    __tablename__ = "whales"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
