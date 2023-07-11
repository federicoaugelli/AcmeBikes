import database.databank as db
from fastapi import FastAPI, status, HTTPException, Depends, Body
from model import payment_body, check_token_body, insert_user, user_login_schema

app = FastAPI()

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

