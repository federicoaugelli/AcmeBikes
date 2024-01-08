import requests, os
from dotenv import load_dotenv

def verify_availability(process_instance_id, process_dict, orderId):
    """ chiamata AcmeDB per verificare disponibilità """
    # in questa fase bisogna vedere se ogni componente è da assemblare o meno
    # se è da assemblare si marca il componente come assegnato
    # se non è da asseblare si cerca il magazzino più vicino al cliente, si calcola il costo della spediione 
    # e successivamente si marca il componente come assegnato
    print(f"availability {orderId}")
    load_dotenv()
    DB_URL = os.getenv("DB_URL")
    GEOLOC_URL = os.getenv("GEOLOC_URL")

    ordered_components = requests.get(f"{DB_URL}/orderedcomponent?orderId={orderId}")
    order = requests.get(f"{DB_URL}/order?order_id={orderId}")
    for ordered_component in ordered_components:
        # Check if the component is assembleable
        component = requests.get(f"{DB_URL}/component?prod_id={ordered_component['componentId']}")
        if not component['assembleable']:
            # Cerca il magazzino più vicino al cliente, si calcola il costo della spedizione
            customer_coordinates = requests.get(f"{GEOLOC_URL}/distance/address?address={order['address']}")
            return {"preventivo": 1000}
    
    # Aggiorna prezzo dell'ordine aggiungendo il costo della spedizione e ritorna il totale
        
    return {"preventivo": 1100}
