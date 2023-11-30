import requests

def verify_customisation(order):
""" chiamata AcmeDB per verificare customizzazione """
    response = requests.get(url, json=order)
    return {"customisation_accepted": response.data}
