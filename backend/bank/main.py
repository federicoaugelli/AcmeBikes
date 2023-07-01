from typing import Union
from fastapi import FastAPI
import database.databank as db
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user")
def register():
    reg = db.register("federico", "frdrk", "password")
    return(reg)

