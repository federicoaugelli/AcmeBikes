import requests

def verify_availability(process_instance_id, process_dict):
    """ chiamata AcmeDB per verificare disponibilità """
    # in questa fase bisogna vedere se ogni componente è da assemblare o meno
    # se è da assemblare si marca il componente come assegnato
    # se non è da asseblare si cerca il magazzino più vicino al cliente, si calcola il costo della spediione 
    # e successivamente si marca il componente come assegnato
    # response = requests.get(url, json=order)
    print("availability")
    return {"preventivo": 1100}
