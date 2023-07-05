from pydantic import BaseModel

class payment_body(BaseModel):
    sender: int
    receiver: int
    amount: float

class check_token_body(BaseModel):
    tx_id: int
    amount: float

class insert_user(BaseModel):
    name: str
    username: str
    password: str

class user_login_schema(BaseModel):
    username: str
    password: str