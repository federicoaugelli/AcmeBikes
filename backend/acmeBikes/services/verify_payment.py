import requests
from dotenv import load_dotenv
import os
import requests

def verify_payment(process_instance_id, process_dict, payment_token, payment_amount):
    print(f"verify_payment {process_instance_id}")
    load_dotenv()
    BANK_URL = os.getenv("BANK_URL")
    ACME_USER = os.getenv("ACME_USER")
    ACME_PASS = os.getenv("ACME_PASS")
    login = requests.post(f"{BANK_URL}/login", json={"username": ACME_USER, "password": ACME_PASS})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    check_token = requests.post(f"{BANK_URL}/checktoken", json={"tx_id": int(payment_token.value), "amount": float(payment_amount.value)}, headers=headers)

    return {"verify_payment": bool(check_token.text)}