import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle

def create_order():
    """ chiamata rivendite per creare l'ordine """
    # response = requests.get(url, json=order)
    print("create_order")
    try:
        start_instance = pycamunda.processdef.StartInstance(url="http://localhost:8080/engine-rest", key='Process_1d9jn7s')
        process_instance = start_instance()

        msg = CorrelateSingle("http://localhost:8080/engine-rest", message_name="order_created",
                              process_instance_id=process_instance.id
                              )
        msg()
    except Exception as e:
        print(e)
        pass
    return {"preventivo": 100}
