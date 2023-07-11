from typing import Union
import requests
from fastapi import FastAPI
from model import component

app = FastAPI()

@app.post("/order", tags=["supplier"])
def get_component(body: component):
   order = body
   return order
    
