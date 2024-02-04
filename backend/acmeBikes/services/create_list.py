import requests
from dotenv import load_dotenv
import os
import requests
from zeep import Client

def create_list(process_instance_id, process_dict, orderId):
    print(f"create_list {process_instance_id}")
    # Comunicare con i magazzini principali o secondari o fornitore esterno per creare la lista dei componenti
    # a seconda della loro posizione e della disponibilità
    load_dotenv()
    DB_URL = os.getenv("DB_URL")
    
    ordered_components = requests.get(f"{DB_URL}/orderedcomponent?orderId={orderId.value}").json()
    all_warehouses = requests.get(f"{DB_URL}/warehouses").json()
    order = requests.get(f"{DB_URL}/order?order_id={orderId.value}").json()
    warehouse_components_lists = {warehouse[0]: [] for warehouse in all_warehouses}
    warehouse_bikes_lists = {warehouse[0]: [] for warehouse in all_warehouses}

    for ordered_component in ordered_components:
        if ordered_component[1] == 0:
            bike = requests.get(f"{DB_URL}/bike/single?Id={ordered_component[2]}").json()
            warehouse_bikes_lists[bike[6]].append({"component_id": bike[0]})
        elif ordered_component[2] == 0:
            component = requests.get(f"{DB_URL}/component/single?Id={ordered_component[1]}").json()
            warehouse_components_lists[component[7]].append({"component_id": component[0], 
                                                             "qty": component[5],
                                                             "assembleable": component[4]})

    client = Client(wsdl='..\\..\\..\\backend\\warehouse\\warehouse.wsdl')

    # Create a request payload
    request_payload = {
        'components': warehouse_components_lists[1]
    }

    # Make the SOAP call
    response = client.service.checkComponents(**request_payload)

    # Print the response
    print(response)
        
    return {"create_list": True}