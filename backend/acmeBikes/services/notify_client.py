import requests

def cancel_order(order_id):
    """ chiamata AcmeDB per eliminare ordine dal DB """
    response = requests.get(url, params=order_id)
    return {"message": response.data}
