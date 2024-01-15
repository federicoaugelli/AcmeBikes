import requests
from dotenv import load_dotenv
import os
import requests

def prepayment(process_instance_id, process_dict):

    amount = 123
    
    load_dotenv()
    BANK_URL = os.getenv("BANK_URL")
    ACME_BANK_ID = os.getenv("ACME_BANK_ID")

    username = "a"
    password = "a"

    login = requests.post(f"{BANK_URL}/login", json={"username": username, "password": password})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get the account id
    user_id = requests.get(f"{BANK_URL}/user", headers=headers).json()["user_id"]

    # pay
    payment = requests.post(f"{BANK_URL}/pay", json={"sender": user_id, "receiver": ACME_BANK_ID, "amount": amount}, headers=headers)


    print(f"prepayment {process_instance_id}")
    return {"prepayment": True}
