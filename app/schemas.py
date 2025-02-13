from pydantic import BaseModel

class WhaleCreate(BaseModel):
    type: str
    latitude: float
    longitude: float

class WhaleResponse(BaseModel):
    id: int
    type: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
