from pydantic import BaseModel

class create_warehouse(BaseModel):
    name: str
    address: str

class create_order(BaseModel):
    price: int
    customer: str
    address: str
    shipment: int

class modify_order(BaseModel):
    order_id: int
    price: int

class apply_discount(BaseModel):
    order_id: int
    perc: int

class add_shipment(BaseModel):
    order_id: int
    shipment: int

class create_ordered_component(BaseModel):
    productId: int
    name: str
    qty: int 
    orderId: int

class create_component(BaseModel):
    productId: int 
    name: str 
    assembleable: bool
    qty: int 
    location: int
