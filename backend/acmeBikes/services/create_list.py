import requests
from dotenv import load_dotenv
import os
import requests

def create_list(process_instance_id, process_dict):
    print(f"create_list {process_instance_id}")
    # Comunicare con i magazzini principali o secondari o fornitore esterno per creare la lista dei componenti
    # a seconda della loro posizione e della disponibilità
    return {"create_list": True}