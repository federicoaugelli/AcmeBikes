from fastapi import FastAPI, status, HTTPException, Depends, Body
from model import geo_distance
from geopy.distance import geodesic

app = FastAPI()

@app.get("/")
def hello():
    return ("hello geolocation")

@app.post("/distance/calculate", tags=["geolocation"])
def calculate_distance(body: geo_distance):
    sender = (body.sender_latitude, body.sender_longitude)
    receiver = (body.receiver_latitude, body.receiver_longitude)
    distance = geodesic(sender, receiver).kilometers
    return(distance)
