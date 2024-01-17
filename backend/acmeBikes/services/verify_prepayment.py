import requests
from dotenv import load_dotenv
import os
import requests

def verify_prepayment(process_instance_id, process_dict, pre_payment_token, pre_payment_amount):
    print(f"verify_prepayment {process_instance_id}")
    load_dotenv()
    print("AA",pre_payment_token, pre_payment_amount)
    BANK_URL = os.getenv("BANK_URL")
    login = requests.post(f"{BANK_URL}/login", json={"username": "luca", "password": "luca"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    check_token = requests.post(f"{BANK_URL}/checktoken", json={"tx_id": int(pre_payment_token.value), "amount": float(pre_payment_amount.value)}, headers=headers)

    return {"verify_prepayment": check_token}