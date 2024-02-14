#modificare orderedcomponent con assemblable

import requests, os, json
from dotenv import load_dotenv

def verify_availability(process_instance_id, process_dict, orderId, order):
    """ chiamata AcmeDB per verificare disponibilità """
    # in questa fase bisogna vedere se ogni componente è da assemblare o meno
    # se è da assemblare si marca il componente come assegnato
    # se non è da asseblare si cerca il magazzino più vicino al cliente, si calcola il costo della spediione 
    # e successivamente si marca il componente come assegnato

    price = 0
    try:
        print(f"availability {orderId.value} - {order.value}")
        load_dotenv()
        DB_URL = os.getenv("DB_URL")
        GEOLOC_URL = os.getenv("GEOLOC_URL")
        COURIER_URL = os.getenv("COURIER_URL")
        order_obj = json.loads(order.value)
        
        # Get all warehouses
        all_warehouses = requests.get(f"{DB_URL}/warehouses").json()
        # Get customer coordinates
        customer_coordinates = requests.post(f"{GEOLOC_URL}/distance/address", json = {"address": order_obj['address']}).json()

        # Get main warehouse
        main_warehouse = next((warehouse for warehouse in all_warehouses if warehouse[1] == "sede principale"), None)

        #calculate shipping cost between main warehouse and customer
        shipment = int(requests.get(f"{COURIER_URL}/shipment/price/{main_warehouse[4]}/{order_obj['address']}").text)

        # Get all bikes
        for bike in order_obj['bikes']:
            bikes = requests.get(f"{DB_URL}/bike?bike_id={bike['productId']}").json()
            min_distance = 10000000
            choosed_bike = None

            # Get the nearest bike
            for _bike in bikes:
                latitude, longitude = next(((warehouse[2], warehouse[3]) for warehouse in all_warehouses if warehouse[0] == _bike[6]), None)
                distance = float(requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": main_warehouse[2],"sender_longitude": main_warehouse[3], "receiver_latitude": latitude,"receiver_longitude": longitude}).text)
                if distance < min_distance:
                    min_distance = distance
                    choosed_bike = _bike 

            # Insert bike in ordered component
            create_ordered_component = {
                "componentId": 0,
                "bikeId": choosed_bike[0],
                "name": choosed_bike[2],
                "qty": bike['qty'], 
                "orderId": orderId.value
            }
            requests.post(f"{DB_URL}/orderedcomponent", json=create_ordered_component)

            # Update bike quantity
            requests.put(f"{DB_URL}/bike?bike_id={choosed_bike[0]}&qty={-1*bike['qty']}")

            price += choosed_bike[3] * bike['qty']

            # Add the components to the order
            for component in bike['components']:
                components = requests.get(f"{DB_URL}/component?prod_id={component['productId']}").json()
                
                # Check if the component is assembleable
                if not components[0][4]:
                    address = ''
                    min_distance = 10000000
                    choosed_component = None

                    # Get the nearest component
                    for _component in components:
                        latitude, longitude, warehouse_address = next(((warehouse[2], warehouse[3], warehouse[4])for warehouse in all_warehouses if warehouse[0] == _component[7]), None)
                        distance = float(requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": customer_coordinates[0],"sender_longitude": customer_coordinates[1], "receiver_latitude": latitude,"receiver_longitude": longitude}).text)
                        if distance < min_distance:
                            min_distance = distance
                            choosed_component = _component
                            address = warehouse_address[4]

                    create_ordered_component = {
                        "componentId": choosed_component[0],
                        "bikeId": 0,
                        "name": choosed_component[2],
                        "qty": component['qty'], 
                        "orderId": orderId.value
                    }
                    requests.post(f"{DB_URL}/orderedcomponent", json=create_ordered_component)

                    # Update component quantity
                    requests.put(f"{DB_URL}/component?prod_id={choosed_component[0]}&qty={-1*component['qty']}")

                    # Calculate shipping cost
                    shipment += int(requests.get(f"{COURIER_URL}/shipment/price/{address}/{order_obj['address']}").text)

                else:
                    #get nearest component to main_warehouse
                    min_distance = 10000000
                    choosed_component = None
                    
                    for _component in components:
                        latitude, longitude = next(((warehouse[2], warehouse[3]) for warehouse in all_warehouses if warehouse[0] == _component[7]), None)
                        distance = float(requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": main_warehouse[2],"sender_longitude": main_warehouse[3], "receiver_latitude": latitude,"receiver_longitude": longitude}).text)
                        if distance < min_distance:
                            min_distance = distance
                            choosed_component = _component

                    create_ordered_component = {
                        "componentId": choosed_component[0],
                        "bikeId": 0,
                        "name": choosed_component[2],
                        "qty": component['qty'], 
                        "orderId": orderId.value
                    }

                    requests.post(f"{DB_URL}/orderedcomponent", json=create_ordered_component)

                    # Update component quantity
                    requests.put(f"{DB_URL}/component?prod_id={choosed_component[0]}&qty={-1*component['qty']}")

                price += sum(_comp[3] * component['qty'] for _comp in components)
                
        #update order price
        requests.put(f"{DB_URL}/order", json={"order_id": orderId.value, "price": price})
        requests.put(f"{DB_URL}/order/shipment", json={"order_id": orderId.value, "shipment": shipment})
    except Exception as e:
        print(e)
        pass
    return {"preventivo": price, "discount": 0}
