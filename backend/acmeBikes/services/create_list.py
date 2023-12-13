import requests
from dotenv import load_dotenv
import os
import requests

def create_list(process_instance_id, process_dict):
    print(f"create_list {process_instance_id}")
    return {"create_list": True}