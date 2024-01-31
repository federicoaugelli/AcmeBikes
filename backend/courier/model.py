from pydantic import BaseModel

class geo_distance(BaseModel):
    sender_latitude: float
    sender_longitude: float
    receiver_latitude: float
    receiver_longitude: float

class user_address(BaseModel):
    address: str

class components(BaseModel):
    component_id: int
    qty: int   
    assembleable: bool
