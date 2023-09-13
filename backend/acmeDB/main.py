import database.dataAcme as db
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
    return ""

@app.post("/order", tags=["order"])
def create_order(body: create_order):
    order = db.insert_order(body.price, body.customer, body.address)
    return(order)

@app.get("/checkIsAssembleable/{component_id}")
def checkIsAssembleable(component_id: str):
    try:
        component = db.get_component(component_id)
        return component.assembleable
    except Exception as e:
        return("error")

@app.post("/orderedcomponent", tags=["ordered Components"])
def create_ordered_component(body: create_ordered_component):
    order = db.insert_order(body.price, body.customer, body.address)
    return(order)

@app.post("/component", tags=["Components"])
def create_component(body: create_component):
    component = db.insert_component(body.productId, body.name, body.assembleable, body.qty, body.bookedQty, body.location)
    return(component)

    

# @app.post("/pay")
# def pay(body: payment_body, dependencies=Depends(JWTBearer())):
#     try:
#         amount = body.amount
#         sender_balance = db.get_user_balance(body.sender)
#         if int(sender_balance[0]) <= amount:
#             return None
#         s = db.update_user_balance(body.sender, -amount)
#         r = db.update_user_balance(body.receiver, amount)
#         tx = db.insert_tx(body.sender, body.receiver, amount)
#         return tx
#     except:
#         return("error")

# @app.post("/checktoken")
# def check_token(body: check_token_body):
#     try:
#         amount = body.amount
#         tx_id = body.tx_id
#         tx = db.get_tx(tx_id)
#         if int(tx[3]) == amount:
#             return True
#         else:
#             return False
#     except:
#         return("error")
