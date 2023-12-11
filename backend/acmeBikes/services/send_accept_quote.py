import requests
import pycamunda
import pycamunda.processdef
from pycamunda.message import CorrelateSingle
from dotenv import load_dotenv
import os

def send_accept_quote(process_instance_id, process_dict):
    """ chiamata AcmeDB per mandare l'accettazione del preventivo """
    load_dotenv()
    CAMUNDA_URL = os.getenv("CAMUNDA_URL")
    print(f"send_accept_quote {process_instance_id}")
    try:
        msg = CorrelateSingle(CAMUNDA_URL, message_name="accepted_quote",
                              process_instance_id=process_dict[process_instance_id]
                              )
        msg()
    except Exception as e:
        print(e)
        pass
    return {"accepted_quote": True}
