import database.dataAcme as db
from fastapi import FastAPI, status, HTTPException, Depends, Body
from model import create_warehouse, create_order, create_ordered_component, create_component 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Database API',
    summary='Database API documentation',
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

#warehouses
@app.get("/warehouse", tags=["warehouse"])
def get_warehouse(warehouseId: int):
    warehouse = db.get_warehouse(warehouseId)
    return(warehouse)

@app.post("/warehouse", tags=["warehouse"])
def create_warehouse(body: create_warehouse):
    warehouse = db.create_warehouse(body.name, body.address)
    return(warehouse)

@app.put("/warehouse", tags=["warehouse"])
def modify_warehouse():
    return 0

@app.delete("/warehouse", tags=["warehouse"])
def delete_warehouse(warehouseId: int):
    warehouse = db.delete_warehouse(warehouseId) 
    return warehouse


#orders
@app.get("/order", tags=["order"])
def get_order():
    return 0

@app.post("/order", tags=["order"])
def create_order(body: create_order):
    order = db.insert_order(body.price, body.customer, body.address)
    return(order)

@app.put("/order", tags=["order"])
def modify_order():
    return 0

@app.delete("/order", tags=["order"])
def cancel_order(order_id: int):
    order = db.insert_order(order_id)
    return(order)


#components
@app.get("/checkIsAssembleable", tags=["components"])
def checkIsAssembleable(component_id: int):
    try:
        component = db.get_component(component_id)
        return component[3]
    except Exception as e:
        return("error")

@app.post("/orderedcomponent", tags=["components"])
def create_ordered_component(body: create_ordered_component):
    order = db.insert_order(body.price, body.customer, body.address)
    return(order)

@app.get("/component", tags=["components"])
def get_components():
    return (0)

@app.post("/component", tags=["components"])
def create_component(body: create_component):
    component = db.insert_component(body.productId, body.name, body.assembleable, body.qty, body.bookedQty, body.location)
    return(component)

@app.put("/component", tags=["components"])
def modify_component():
    return 0

@app.delete("/component", tags=["components"])
def delete_component():
    return (0)

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
