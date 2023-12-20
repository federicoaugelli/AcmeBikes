import requests

def verify_availability(process_instance_id, process_dict, orderId):
    """ chiamata AcmeDB per verificare disponibilità """
    # in questa fase bisogna vedere se ogni componente è da assemblare o meno
    # se è da assemblare si marca il componente come assegnato
    # se non è da asseblare si cerca il magazzino più vicino al cliente, si calcola il costo della spediione 
    # e successivamente si marca il componente come assegnato
    print(f"availability {orderId}")
    # ordered_components = requests.get("/orderedcomponents", json=orderId)
    # for ordered_component in ordered_components:
    #     # Check if the component is assembleable
    #     isAssembleable = requests.get(f"/isAssembleable?component_id={ordered_component.componentId}")
    #     if not isAssembleable:
    #         # Cerca il magazzino più vicino al cliente, si calcola il costo della spedizione 
    #         return {"preventivo": 1000}
    
    # Aggiorna prezzo dell'ordine aggiungendo il costo della spedizione e ritorna il totale
        
    return {"preventivo": 1100}
