from sqlalchemy.orm import Session
from . import models, schemas
from geopy.distance import geodesic


def create_whale(db: Session, whale: schemas.WhaleCreate):
    db_whale = models.Whale(**whale.dict())
    db.add(db_whale)
    db.commit()
    db.refresh(db_whale)
    return db_whale


def get_closest_whale(db: Session, latitude: float, longitude: float):
    whales = db.query(models.Whale).all()
    if not whales:
        return None
    user_location = (latitude, longitude)
    closest_whale = min(
        whales,
        key=lambda whale: geodesic(user_location, (whale.latitude, whale.longitude)).m
    )
    return closest_whale
