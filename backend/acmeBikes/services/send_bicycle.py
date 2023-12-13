import requests
from dotenv import load_dotenv
import os
import requests

def send_bicycle(process_instance_id, process_dict):
    print(f"send_bicycle {process_instance_id}")
    # Comunicare col corriere e mandargli process instance id del resale
    return {"send_bicycle": True}