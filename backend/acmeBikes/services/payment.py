import requests
from dotenv import load_dotenv
import os
import requests, json
import pycamunda.processdef
from pycamunda.message import CorrelateSingle

def payment(process_instance_id, process_dict, order):
    # TODO: richiesta al db per cancellare ordine e finire
    print(f"payment {process_instance_id}")
    order_obj = json.loads(order.value)
    total_price = order_obj[1] + order_obj[4]
    amount = (total_price / 100) * 90

    load_dotenv()
    BANK_URL = os.getenv("BANK_URL")
    ACME_BANK_ID = os.getenv("ACME_BANK_ID")
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")

    username = "a"
    password = "a"
    login = requests.post(f"{BANK_URL}/login", json={"username": username, "password": password})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get the account id
    user_id = requests.get(f"{BANK_URL}/user", headers=headers).json()["user_id"]

    # pay
    payment = requests.post(f"{BANK_URL}/pay", json={"sender": user_id, "receiver": ACME_BANK_ID, "amount": amount}, headers=headers)

    process_instance_id = process_dict[process_instance_id]
    try:
        msg = CorrelateSingle(CAMUNDA_URL, message_name="token_payment",
                            process_instance_id=process_instance_id, result_enabled=False
                            )
        msg.add_process_variable(name="payment_token", value=payment.text)
        msg.add_process_variable(name="payment_amount", value=amount)
        msg()
    except Exception as e:
        print(e)
        pass    
    return {"payment": True}