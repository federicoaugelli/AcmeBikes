import requests, json, os
from dotenv import load_dotenv

def verify_customisation(process_instance_id, process_dict, order):
    """ chiamata AcmeDB per verificare customizzazione """
    print(f"customisation {order}")

    load_dotenv()
    DB_URL = os.getenv("DB_URL")

    order_obj = json.loads(order.value)
    
    # Check if the bike is customisable
    for bike in order_obj['bikes']:
        for component in bike['components']:
            isCustomisable = requests.get(f"{DB_URL}/custom?bike_id={bike['bikeId']}&component_id={component['componentId']}")
            if not isCustomisable:
                return {"isCustomisable": False}
            
    # If the bike is customisable, create the order
    create_order = {
        "price": 0,
        "customer": order_obj['customer'],
        "address": order_obj['address'],
        "shipment": 0,
    }
    created_order = requests.post(f"{DB_URL}/order", json=create_order)
    create_order_id = int(created_order.text)
    print(f"ordine {created_order.text}")
    # Add the bikes to the order
    '''for bike in order_obj['bikes']:
        create_ordered_component = {
            "componentId": 0,
            "bikeId": bike['bikeId'],
            "name": "Nome bici",
            "qty": bike['qty'], 
            "orderId": create_order_id
        }
        requests.post(f"{DB_URL}/orderedcomponent", json=create_ordered_component)
        # Add the components to the order
        for component in bike['components']:
            create_ordered_component = {
                "componentId": component['componentId'],
                "bikeId": 0,
                "name": "Nome componente",
                "qty": component['qty'], 
                "orderId": create_order_id
            }
            requests.post(f"{DB_URL}/orderedcomponent", json=create_ordered_component)'''

    return {"isCustomisable": True, "orderId": create_order_id, "order": order_obj} 
