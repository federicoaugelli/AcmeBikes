from typing import List, Union
import requests
from fastapi import FastAPI
from model import components, components_list
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Supplier API',
    summary='Supplier API documentation',
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/supplier", tags=["supplier"])
def get_component(body: List[components]):
   order = body
   return "OK"
    
