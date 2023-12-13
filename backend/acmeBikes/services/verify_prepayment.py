import requests
from dotenv import load_dotenv
import os
import requests

def verify_prepayment(process_instance_id, process_dict):
    print(f"verify_prepayment {process_instance_id}")
    return {"verify_prepayment": True}