import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os, json

def create_order(process_instance_id, process_dict):
    """ chiamata rivendite per creare l'ordine """
    #per creare l'ordine bisogna mandere ad acme bike l'elenco dei cicli con eventuali castomizzazioni
    #l'elenco ci viene formito dal frontend
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    ACMEBIKE_KEY = os.getenv("ACMEBIKE_KEY")
    print(f"create_order {process_instance_id}")
    try:
        order = {
            "customer": "Michele Abruzzese",
            "address": "via ercolani 1, Bologna",
            "bikes": [
                {
                    "productId": 4123,
                    "qty": 1,
                    "components": [
                        {
                            "productId": 5192,
                            "qty": 1
                        },
                        {
                            "productId": 6532,
                            "qty": 1
                        }
                    ]
                },
            ]
        }
        start_instance = pycamunda.processdef.StartInstance(url=CAMUNDA_URL, key=ACMEBIKE_KEY)
        start_instance.add_variable(name="order", value=json.dumps(order))
        process_instance = start_instance()
        process_dict[process_instance_id] = process_instance.id_
        
        msg = CorrelateSingle(CAMUNDA_URL, message_name="order_created",
                            process_instance_id=process_instance.id_, result_enabled=False
                            )
        msg()
    except Exception as e:
        print(e)
        pass
    return {"order_created": True}
