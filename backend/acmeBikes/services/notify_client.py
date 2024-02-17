import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os

def notify_client(process_instance_id, process_dict):
    # in questo caso non bisogna fare nulla con il db perchè non abbiamo ancora marcato i pezzi, 
    # ma abbiamo controllato solo la fattibilità della customizzazione
    #devo solo dire alla rivendita che la customizzazione non è fattibile
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    print(f"notify_client {process_instance_id}")
    try:
        
        # list out keys and values separately
        key_list = list(process_dict.keys())
        val_list = list(process_dict.values())        
        # print key with val 100
        position = val_list.index(process_instance_id)
        resale_process_instance_id = key_list[position]

        process_dict[process_instance_id] = resale_process_instance_id
        
        msg = CorrelateSingle(CAMUNDA_URL, message_name="order_not_accepted",
                              process_instance_id=resale_process_instance_id
                              )
        msg()
    except Exception as e:
        print(e)
        pass
    return {"order_canceled": True}
