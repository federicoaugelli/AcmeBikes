import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os

def send_quote(process_instance_id, process_dict, orderId):
    """ chiamata AcmeDB per mandare il preventivo """
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    DB_URL = os.getenv("DB_URL")
    print(f"send_quote {process_instance_id}")
    try:
        order = requests.get(f"{DB_URL}/order?order_id={orderId.value}").json()
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
        msg.add_process_variable(name="order", value=order)
        # Mando anche preventivo e spedizione per mostrarli sul camunda form, sarà poi da mandare a frontend
        msg.add_process_variable(name="price", value=order[1])
        msg.add_process_variable(name="shipment", value=order[4])
        msg()
    except Exception as e:
        print(e)
        pass
    return {"order_accepted": True}
