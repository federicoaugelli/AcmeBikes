import database.dataAcme as db
from fastapi import FastAPI, status, HTTPException, Depends, Body
from model import create_warehouse, create_order, create_ordered_component, create_component, modify_order, apply_discount, add_shipment
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




'''WAREHOUSES'''
@app.get("/warehouse", tags=["warehouse"])
def get_warehouse(warehouseId: int):
    warehouse = db.get_warehouse(warehouseId)
    return(warehouse)

@app.post("/warehouse", tags=["warehouse"])
def create_warehouse(body: create_warehouse):
    warehouse = db.create_warehouse(body.name, body.address)
    return(warehouse)

#da fare
@app.put("/warehouse", tags=["warehouse"])
def modify_warehouse():
    return 0

@app.delete("/warehouse", tags=["warehouse"])
def delete_warehouse(warehouseId: int):
    warehouse = db.delete_warehouse(warehouseId) 
    return warehouse





'''ORDER'''
@app.get("/order", tags=["order"])
def get_order(order_id: int, customer: str):
    try:
        order = db.get_order(order_id, customer)
        return order
    except Exception as e:
        return e

@app.post("/order", tags=["order"])
def create_order(body: create_order):
    order = db.insert_order(body.price, body.customer, body.address, body.shipment)
    return(order)

@app.put("/order", tags=["order"])
def modify_order(body: modify_order):
    order = db.modify_order(body.order_id, body.price)
    return order

@app.delete("/order", tags=["order"])
def cancel_order(order_id: int):
    try:
        order = db.cancel_order(order_id)
        return(order)
    except Exception as e:
        return e

@app.put("/order/discount", tags=["order"])
def apply_discount(body: apply_discount):
    order = db.apply_discount(body.order_id, body.perc)
    return order

@app.put("/order/shipment", tags=["order"])
def shipment(body: add_shipment):
    order = db.add_shipment(body.order_id, body.shipment)
    return order



'''ASSEMBLABLE'''
@app.get("/checkIsAssembleable", tags=["components"])
def checkIsAssembleable(component_id: int):
    try:
        component = db.get_component(component_id)
        return component[3]
    except Exception as e:
        return("error")




'''ORDERED COMPONENT'''
@app.get("/orderedcomponent", tags=["ordered components"])
def get_ordered_component(orderId: int):
    order = db.get_ordered_component(orderId)
    return(order)

@app.post("/orderedcomponent", tags=["ordered components"])
def create_ordered_component(body: create_ordered_component):
    order = db.insert_ordered_component(body.productId, body.name, body.qty, body.orderId)
    return(order)

@app.delete("/orderedcomponent", tags=["ordered components"])
def get_ordered_component(orderId: int):
    order = db.cancel_ordered_component(orderId)
    return(order)






'''COMPONENTS'''
@app.get("/component", tags=["components"])
def get_components(prod_id: int):
    try:
        component = db.get_component(prod_id)
        return(component)
    except Exception as e:
        return e

@app.post("/component", tags=["components"])
def create_component(body: create_component):
    component = db.insert_component(body.productId, body.name, body.assembleable, body.qty, body.bookedQty, body.location)
    return(component)

@app.put("/component", tags=["components"])
def modify_component(prod_id: int, qty: int):
    try:
        component = db.modify_component(prod_id, qty)
        return(component)
    except Exception as e:
        return e

@app.delete("/component", tags=["components"])
def delete_component(prod_id: int):
    try:
        component = db.cancel_component(prod_id)
        return(component)
    except Exception as e:
        return e

