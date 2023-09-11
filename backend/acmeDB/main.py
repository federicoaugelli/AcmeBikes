import database.databank as db
from fastapi import FastAPI, status, HTTPException, Depends, Body
from model import create_warehouse, create_order, create_ordered_component, create_component 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/warehouse", tags=["warehouse"])
def create_warehouse(body: create_warehouse):
    warehouse = db.create_warehouse(body.name, body.address)
    return(warehouse)

@app.delete("/warehouse", tags=["warehouse"])
def delete_warehouse():

@app.post("/order", tags=["order"])
def create_warehouse(body: create_warehouse):
    order = db.insert_order(body.price, body.customer, body.address)
    return(order)



@app.post("/orderedcomponent", tags=["ordered Components"])
def create_warehouse(body: create_warehouse):
    order = db.insert_order(body.price, body.customer, body.address)
    return(order)

    

@app.post("/pay")
def pay(body: payment_body, dependencies=Depends(JWTBearer())):
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
