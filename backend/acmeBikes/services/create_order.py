import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os

def create_order(process_instance_id, process_dict):
    """ chiamata rivendite per creare l'ordine """
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    ACMEBIKE_KEY = os.getenv("ACMEBIKE_KEY")
    print(CAMUNDA_URL)
    # response = requests.get(url, json=order)
    print(f"create_order {process_instance_id}")
    try:
        start_instance = pycamunda.processdef.StartInstance(url=CAMUNDA_URL, key=ACMEBIKE_KEY)
        process_instance = start_instance()
        process_dict[process_instance_id] = process_instance.id_
        
        msg = CorrelateSingle(CAMUNDA_URL, message_name="order_created",
                              process_instance_id=process_instance.id_
                              )
        msg()
    except Exception as e:
        print(e)
        pass
    return {"preventivo": 100}
