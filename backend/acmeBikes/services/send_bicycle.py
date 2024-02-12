import requests
from dotenv import load_dotenv
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
import os, json
import requests

def send_bicycle(process_instance_id, process_dict, components_for_resale):
    print(f"send_bicycle {process_instance_id}")
    # Comunicare col corriere e mandargli process instance id del resale
    load_dotenv()
    COURIER_URL = os.getenv("COURIER_URL")
    components_for_resale_obj = json.loads(components_for_resale.value)
    try:
        # list out keys and values separately
        key_list = list(process_dict.keys())
        val_list = list(process_dict.values())        
        position = val_list.index(process_instance_id)
        resale_process_instance_id = key_list[position]
        components_for_resale_obj["contact_resale"] = True
        components_for_resale_obj["resale_instance_id"] = resale_process_instance_id
        
        requests.post(f"{COURIER_URL}/shipment", json=components_for_resale_obj)
    except Exception as e:
        print(e)
        pass
    return {"send_bicycle": True}