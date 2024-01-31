from typing import Union
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from model import components

app = FastAPI(
    title='Courier API',
    summary='Courier API documentation',
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

geoUrl = "http://127.0.0.1:8002"
tariffa = 0.2

@app.get("/shipment/price/{sender}/{receiver}", tags=["courier"])
def get_price_by_places(sender: str, receiver: str):
    sender_location = requests.post(geoUrl + "/distance/address", json={"address": sender}).json()
    receiver_location = requests.post(geoUrl + "/distance/address", json={"address": receiver}).json()
    distance = requests.post(geoUrl + "/distance/calculate", json={"sender_latitude": sender_location[0],"sender_longitude": sender_location[1],"receiver_latitude": receiver_location[0],"receiver_longitude": receiver_location[1]}).json()
    price = distance*tariffa
    return int(price)

@app.post("/shipment", tags=["courier"])
def shipment(components: List[components]):
    return "Shipped"
