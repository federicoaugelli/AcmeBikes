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
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    components_for_resale_obj = json.loads(components_for_resale.value)
    try:
        # list out keys and values separately
        key_list = list(process_dict.keys())
        val_list = list(process_dict.values())        
        position = val_list.index(process_instance_id)
        resale_process_instance_id = key_list[position]
                
        msg = CorrelateSingle(CAMUNDA_URL, message_name="components_received",
                              process_instance_id=resale_process_instance_id
                              )
        msg.add_process_variable(name="components", value=json.dumps(components_for_resale_obj))
        msg()
    except Exception as e:
        print(e)
        pass
    return {"send_bicycle": True}