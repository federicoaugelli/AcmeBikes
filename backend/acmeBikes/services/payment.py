import requests
from dotenv import load_dotenv
import os
import requests

def payment(process_instance_id, process_dict):
    # TODO: richiesta al db per cancellare ordine e finire
    print(f"payment {process_instance_id}")
    return {"payment": True}