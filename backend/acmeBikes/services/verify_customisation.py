import requests

def verify_customisation():
    """ chiamata AcmeDB per verificare customizzazione """
    # response = requests.get(url, json=order)
    print("customisation")
    return {"isCustomisable": True}