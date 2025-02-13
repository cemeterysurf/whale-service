from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/whales/", response_model=schemas.WhaleResponse)
def create_whale(whale: schemas.WhaleCreate, db: Session = Depends(get_db)):
    return crud.create_whale(db, whale=whale)


@app.get("/closest-whale/", response_model=schemas.WhaleResponse)
def get_closest_whale(latitude: float, longitude: float, db: Session = Depends(get_db)):
    whale = crud.get_closest_whale(db, latitude=latitude, longitude=longitude)
    if whale is None:
        raise HTTPException(status_code=404, detail="No whales found")
    return whale
