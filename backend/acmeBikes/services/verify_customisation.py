import requests

def verify_customisation(process_instance_id, process_dict):
    """ chiamata AcmeDB per verificare customizzazione """
    # response = requests.get(url, json=order)
    print("customisation")
    print(process_dict)
    return {"isCustomisable": True}