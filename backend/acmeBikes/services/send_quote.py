def send_quote(process_instance_id, process_dict, discount):
    """ chiamata AcmeDB per verificare customizzazione """
    print(discount)
    return {"quote": discount}