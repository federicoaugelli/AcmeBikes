import requests

def verify_availability(order):
""" chiamata AcmeDB per verificare disponibilità """
    response = requests.get(url, json=order)
    return {"preventivo": response.data}
