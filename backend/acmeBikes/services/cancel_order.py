import requests
from dotenv import load_dotenv
import os
import requests

def cancel_order(process_instance_id, process_dict, orderId):
    print(f"cancel_order {process_instance_id}")
    load_dotenv()
    DB_URL = os.getenv("DB_URL")
    ordered_components = requests.get(f"{DB_URL}/orderedcomponent?orderId={orderId.value}").json()
    for ordered_component in ordered_components:
        if ordered_component[1] == 0:
            requests.put(f"{DB_URL}/bike", json={"bike_id":ordered_component[2], "qty":ordered_component[4]})
        elif ordered_component[2] == 0:
            requests.put(f"{DB_URL}/component", json={"prod_id":ordered_component[1], "qty":ordered_component[4]})
            
    requests.delete(f"{DB_URL}/orderedcomponent?orderId={orderId.value}")
    requests.delete(f"{DB_URL}/order?order_id={orderId.value}")

    return {"order_canceled": True}