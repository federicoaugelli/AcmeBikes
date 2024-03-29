import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os, json

def send_quote(process_instance_id, process_dict, orderId, discount):
    """ chiamata AcmeDB per mandare il preventivo """
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    DB_URL = os.getenv("DB_URL")
    print(f"send_quote {process_instance_id}")
    try:
        order = requests.get(f"{DB_URL}/order?order_id={orderId.value}").json()
        if discount.value != 0:
            order = requests.put(f"{DB_URL}/order/discount", json={"order_id": order[0], "perc": discount.value}).json()
        # list out keys and values separately
        key_list = list(process_dict.keys())
        val_list = list(process_dict.values())        
        position = val_list.index(process_instance_id)
        resale_process_instance_id = key_list[position]
        
        process_dict[process_instance_id] = resale_process_instance_id
        
        msg = CorrelateSingle(CAMUNDA_URL, message_name="order_accepted",
                              process_instance_id=resale_process_instance_id
                              )
        msg.add_process_variable(name="order", value=json.dumps(order))
        msg.add_process_variable(name="price", value=order[1])
        msg.add_process_variable(name="shipment", value=order[4])
        msg()
    except Exception as e:
        print(e)
        pass
    return {"order_accepted": True}
