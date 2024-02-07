from pydantic import BaseModel
from typing import List

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

class components_list(BaseModel):
    resale_instance_id: str
    components: List[components]