import requests
from dotenv import load_dotenv
import os
import requests

def prepayment(process_instance_id, process_dict):
    print(f"prepayment {process_instance_id}")
    return {"prepayment": True}