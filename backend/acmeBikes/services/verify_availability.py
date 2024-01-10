import requests, os
from dotenv import load_dotenv

def verify_availability(process_instance_id, process_dict, orderId, order):
    """ chiamata AcmeDB per verificare disponibilità """
    # in questa fase bisogna vedere se ogni componente è da assemblare o meno
    # se è da assemblare si marca il componente come assegnato
    # se non è da asseblare si cerca il magazzino più vicino al cliente, si calcola il costo della spediione 
    # e successivamente si marca il componente come assegnato



    print(f"availability {orderId.value}")
    load_dotenv()
    DB_URL = os.getenv("DB_URL")
    GEOLOC_URL = os.getenv("GEOLOC_URL")

    ordered_components = requests.get(f"{DB_URL}/orderedcomponent?orderId={orderId.value}")
    order = requests.get(f"{DB_URL}/order?order_id={orderId.value}")
    all_warehouses = requests.get(f"{DB_URL}/warehouses")
    for ordered_component in ordered_components:
        # Check if the component is assembleable
        component = requests.get(f"{DB_URL}/component?prod_id={ordered_component[1]}")
        print(f"ordered_component: {ordered_component.text}")
        #print(f"component: {component.text}")
        component = component.json()
        if not component[4]:
            # Cerca il magazzino più vicino al cliente, si calcola il costo della spedizione
            customer_coordinates = requests.get(f"{GEOLOC_URL}/distance/address?address={int(order['address'])}")
            min_distance = 10000000
            warehouse_id = None
            for warehouse in all_warehouses:
                distance = requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": customer_cordinates[0],"sender_longitude": customer_cordinates[1], "receiver_latitude": warehouse[1],"receiver_longitude": warehouse[2]})
                if distance < min_distance:
                    min_distance = distance
                    warehouse_id = warehouse[0]
            print(f"warehouse_id: {warehouse_id}")
            print(f"min_distance: {min_distance}")

            return {"preventivo": 1000}
    
    # Aggiorna prezzo dell'ordine aggiungendo il costo della spedizione e ritorna il totale
        
    return {"preventivo": 1100}
