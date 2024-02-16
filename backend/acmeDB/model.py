from pydantic import BaseModel

class create_warehouse(BaseModel):
    name: str
    address: str
    port: int

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
    componentId: int
    bikeId: int
    name: str
    qty: int 
    orderId: int

class create_component(BaseModel):
    productId: int 
    name: str 
    price: int
    assembleable: bool
    qty: int
    ty: str
    location: int

class modify_component(BaseModel):
    prod_id: int
    qty: int

class create_bike(BaseModel):
    productId: int
    name: str
    price: int
    qty: int
    color: str
    location: int

class modify_bike(BaseModel):
    bike_id: int
    qty: int

class create_customisation(BaseModel):
    bikeId: int
    componentId: int
