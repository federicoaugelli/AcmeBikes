from pydantic import BaseModel
from typing import List

class components(BaseModel):
    component_id: int
    qty: int   
    assembleable: bool

class components_list(BaseModel):
    components: List[components]




