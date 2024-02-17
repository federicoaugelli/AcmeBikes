import database.databank as db
from fastapi import FastAPI, status, HTTPException, Depends, Body
import auth.crypt_utils as crypt_utils
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT, decodeJWT
from model import payment_body, check_token_body, insert_user, user_login_schema
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Bank API',
    summary='Bank API documentation',
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login", tags=["user"])
def user_login(body: user_login_schema = Body(...)):
    user = db.get_user_by_username(body.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )

    hashed_pass = user[4]
    if not crypt_utils.verify_password(body.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    # I sign it with user id
    return signJWT(user[0])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/user", tags=["user"])
def user_login_schema(body: insert_user):
    user_data = db.insert_user(body.name, body.username, crypt_utils.get_hashed_password(body.password))
    return(user_data)

@app.get("/user", tags=["user"])
def get_user(user_data: str = Depends(JWTBearer()), dependencies=Depends(JWTBearer())):
    try:
        data = decodeJWT(user_data)
        return data
    except Exception as e:
        return e

@app.post("/pay")
def pay(body: payment_body, dependencies=Depends(JWTBearer())):
    try:
        amount = body.amount
        sender_balance = db.get_user_balance(body.sender)
        if int(sender_balance[0]) <= amount:
            return None
        s = db.update_user_balance(body.sender, -amount)
        r = db.update_user_balance(body.receiver, amount)
        tx = db.insert_tx(body.sender, body.receiver, amount)
        return tx
    except:
        return("error")

@app.post("/checktoken")
def check_token(body: check_token_body):
    try:
        amount = body.amount
        tx_id = body.tx_id
        tx = db.get_tx(tx_id)
        if int(tx[3]) == amount:
            return True
        return False
    except:
        return False

