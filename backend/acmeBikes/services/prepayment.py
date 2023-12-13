import requests
from dotenv import load_dotenv
import os
import requests

def prepayment(process_instance_id, process_dict):
    # TODO: richiesta al db per cancellare ordine e finire
    print(f"prepayment {process_instance_id}")
    return {"prepayment": True}