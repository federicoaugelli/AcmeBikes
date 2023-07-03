from typing import Union
from fastapi import FastAPI
import database.databank as db
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

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user")
def user(body: insert_user):
    user_data = db.insert_user(body.name, body.username, body.password)
    return(user_data)

@app.post("/pay")
def pay(body: payment_body):
    try:
        amount = body.amount
        sender_balance = db.get_user_balance(body.sender)
        if int(sender_balance[0]) <= amount:
            return None
        s = db.update_user_balance(body.sender, -amount)
        r = db.update_user_balance(body.receiver, amount)
        tx = db.insert_tx(body.sender, body.receiver, amount)
        return tx
    except:
        return("error")

@app.post("/checktoken")
def check_token(body: check_token_body):
    try:
        amount = body.amount
        tx_id = body.tx_id
        tx = db.get_tx(tx_id)
        if int(tx[3]) == amount:
            return True
        else:
            return False
    except:
        return("error")

