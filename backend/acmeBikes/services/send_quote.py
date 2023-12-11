import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os

def send_quote(process_instance_id, process_dict, discount):
    """ chiamata AcmeDB per mandare il preventivo """
    print(discount)
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    print(f"send_quote {process_instance_id}")
    try:
        # list out keys and values separately
        key_list = list(process_dict.keys())
        val_list = list(process_dict.values())        
        # print key with val 100
        position = val_list.index(process_instance_id)
        resale_process_instance_id = key_list[position]
        
        process_dict[process_instance_id] = resale_process_instance_id
        
        msg = CorrelateSingle(CAMUNDA_URL, message_name="order_accepted",
                              process_instance_id=resale_process_instance_id
                              )
        msg()
    except Exception as e:
        print(e)
        pass
    return {"order_accepted": True}
