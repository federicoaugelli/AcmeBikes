import requests
from dotenv import load_dotenv
import os
import requests

def cancel_order(process_instance_id, process_dict):
    # TODO: richiesta al db per cancellare ordine e finire
    print(f"cancel_order {process_instance_id}")
    return {"order_canceled": True}