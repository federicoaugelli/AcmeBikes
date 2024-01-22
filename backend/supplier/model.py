from pydantic import BaseModel
from typing import List

class components_list(BaseModel):
    productIds: List[int]



