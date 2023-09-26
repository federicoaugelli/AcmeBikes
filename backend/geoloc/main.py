from fastapi import FastAPI, status, HTTPException, Depends, Body
from model import geo_distance, user_address
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Geoloc API',
    summary='Geoloc API documentation',
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
def hello():
    return ("hello geolocation")

@app.post("/distance/calculate", tags=["geolocation"])
def calculate_distance(body: geo_distance):
    sender = (body.sender_latitude, body.sender_longitude)
    receiver = (body.receiver_latitude, body.receiver_longitude)
    distance = geodesic(sender, receiver).kilometers
    return(distance)

@app.post("/distance/address", tags=["geolocation"])
def retreive_address(body: user_address):
    geolocator = Nominatim(user_agent="my_app")
    address = body.address
    location = geolocator.geocode(address)
    return location.latitude, location.longitude
