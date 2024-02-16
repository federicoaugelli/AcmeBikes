import requests
from dotenv import load_dotenv
import os
import requests, json
from zeep import Client

def create_list(process_instance_id, process_dict, orderId):
    print(f"create_list {process_instance_id}")
    # Comunicare con i magazzini principali o secondari o fornitore esterno per creare la lista dei componenti
    # a seconda della loro posizione e della disponibilità
    load_dotenv()
    DB_URL = os.getenv("DB_URL")

    # list out keys and values separately
    key_list = list(process_dict.keys())
    val_list = list(process_dict.values())        
    position = val_list.index(process_instance_id)
    resale_process_instance_id = key_list[position]
    
    ordered_components = requests.get(f"{DB_URL}/orderedcomponent?orderId={orderId.value}").json()
    all_warehouses = requests.get(f"{DB_URL}/warehouses").json()
    all_warehouses = [warehouse for warehouse in all_warehouses if warehouse[0] != 1]
    warehouse_components_lists = {warehouse[0]: [] for warehouse in all_warehouses}
    warehouse_bikes_lists = {warehouse[0]: [] for warehouse in all_warehouses}

    for ordered_component in ordered_components:
        if ordered_component[1] == 0:
            bike = requests.get(f"{DB_URL}/bike/single?Id={ordered_component[2]}").json()
            warehouse_bikes_lists[bike[6]].append({"bike_id": bike[0],
                                                   "qty": bike[4],
                                                   "ordered_qty": ordered_component[4] })
        elif ordered_component[2] == 0:
            component = requests.get(f"{DB_URL}/component/single?Id={ordered_component[1]}").json()
            warehouse_components_lists[component[7]].append({"component_id": component[0], 
                                                             "qty": component[5],
                                                             "ordered_qty": ordered_component[4],
                                                             "assembleable": component[4]})

    #mainWarehouseClient = Client(wsdl='..\\..\\..\\backend\\warehouse\\warehouse.wsdl')
    mainWarehouseClient = Client(wsdl='../../../backend/warehouse/warehouse.wsdl')
    #secondaryWarehouseClient = Client(wsdl='..\\..\\..\\backend\\warehouse\\secondaryWarehouse.wsdl')
    secondaryWarehouseClient = Client(wsdl='../../../backend/warehouse/secondaryWarehouse.wsdl')

    components_for_resale = {
        "components": [],
        "bikes": []
    }

    # Create a request payload
    for warehouse in all_warehouses:
        request_payload = {
            'resale_instance_id': resale_process_instance_id,
            'components': warehouse_components_lists[warehouse[0]]
        }

        bike_request_payload = {
            'bikes': warehouse_bikes_lists[warehouse[0]]
        }

        component_response = {}
        bike_response = {}
        # Make the SOAP call
        if warehouse[1] == "magazzino principale":
            if warehouse_components_lists[warehouse[0]]:
                component_response = mainWarehouseClient.service.checkComponents(**request_payload)
            if warehouse_bikes_lists[warehouse[0]]:
                bike_response = mainWarehouseClient.service.checkBikes(**bike_request_payload)
        else:
            if warehouse_components_lists[warehouse[0]]:
                component_response = secondaryWarehouseClient.service.checkComponents(**request_payload)
            if warehouse_bikes_lists[warehouse[0]]:
                bike_response = secondaryWarehouseClient.service.checkBikes(**bike_request_payload)
        
        # add to components_for_resale components and bikes the response of the SOAP call. check that the fields are not empty object or none
        if component_response:
            components_for_resale["components"].extend(component_response.components)
        if bike_response:
            components_for_resale["bikes"].extend(bike_response.bikes)
        
    return {"components_for_resale": json.dumps(components_for_resale)}
