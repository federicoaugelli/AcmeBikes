import requests

def cancel_order(process_instance_id, process_dict, order_id):
    """ chiamata AcmeDB per eliminare ordine dal DB """
    response = requests.get(url, params=order_id)
    return {"message": response.data}
