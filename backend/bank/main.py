from typing import Union
from fastapi import FastAPI
import database.databank as db
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.route("/user", methods=["POST, DELETE"])
def user():
    if request.method == "POST":
        user_data = db.insert_user("federico", "frdrk", "password")
        return(user_data)

    #elif request.method == "DELETE":

'''
@app.route("/user/balance", methods=["GET", "POST"])
def balance():
    if request.method == "GET":
        user_balance = db.get_user_balance()
        return user_balance
    else:
        user_balance = db.update_user_balance()

@app.route("/transaction", methods=["GET", "POST"])
def tx():
    if request.method == "GET":
        tx = db.get_tx()
        return tx
    else:
        tx = db.insert_tx()
        return tx
'''
