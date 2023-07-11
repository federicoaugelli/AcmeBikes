from pydantic import BaseModel

class payment_body(BaseModel):
    sender: int
    receiver: int
    amount: float


