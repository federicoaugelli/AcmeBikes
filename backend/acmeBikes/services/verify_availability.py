#modificare orderedcomponent con assemblable

import requests, os, json
from dotenv import load_dotenv

def verify_availability(process_instance_id, process_dict, orderId, order):
    """ chiamata AcmeDB per verificare disponibilità """
    # in questa fase bisogna vedere se ogni componente è da assemblare o meno
    # se è da assemblare si marca il componente come assegnato
    # se non è da asseblare si cerca il magazzino più vicino al cliente, si calcola il costo della spediione 
    # e successivamente si marca il componente come assegnato

    print(f"availability {orderId.value}")
    load_dotenv()
    DB_URL = os.getenv("DB_URL")
    GEOLOC_URL = os.getenv("GEOLOC_URL")
    COURIER_URL = os.getenv("COURIER_URL")
    order_obj = json.loads(order.value)
    


    # Get all warehouses
    all_warehouses = requests.get(f"{DB_URL}/warehouses")

    # Get customer coordinates
    customer_cordinates = requests.get(f"{GEOLOC_URL}/distance/address?address={order_obj['address']}")

    # Get main warehouse
    main_warehouse = next((warehouse for warehouse in all_warehouses if warehouse[1] == "magazzino principale"), None)

    price = 0
    shipment = 0

    #calculate shipping cost between main warehouse and customer
    shipment += reqeusts.get(f"{COURIER_URL}/shipment/price/{main_warehouse[4]}/{order_obj['address']}").json()


    # Get all bikes
    for bike in order_obj['bikes']:
        bikes = requests.get(f"{DB_URL}/bike?prod_id={bike['productId']}").json()
        min_distance = 10000000
        choosed_bike = None

        # Get the nearest bike
        for _bike in bikes:
            latitude, longitude = next((warehouse[2], warehouse[3] for warehouse in all_warehouses if warehouse[0] == _bike[6]), None)
            distance = requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": main_warehouse[2],"sender_longitude": main_warehouse[3], "receiver_latitude": latitude,"receiver_longitude": longitude})
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
                    latitude, longitude = next((warehouse[2], warehouse[3] for warehouse in all_warehouses if warehouse[0] == _component[7]), None)
                    distance = requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": customer_coordinates[0],"sender_longitude": customer_coordinates[1], "receiver_latitude": latitude,"receiver_longitude": longitude})
                    if distance < min_distance:
                        min_distance = distance
                        choosed_component = _component
                        address = warehouse[4]
                
                    


                create_ordered_component = {
                    "componentId": choosed_component[0],
                    "bikeId": 0,
                    "name": choosed_component[2],
                    "qty": component['qty'], 
                    "orderId": orderId.value
                }
                requests.post(f"{DB_URL}/orderedcomponent", json=create_ordered_component)

                # Update component quantity
                requests.put(f"{DB_URL}/component?component_id={choosed_component[0]}&qty={-1*component['qty']}")

                # Calculate shipping cost
                shipment += requests.get(f"{COURIER_URL}/shipment/price/{address}/{order_obj['address']}").json()

            else:
                #get nearest component to main_warehouse
                min_distance = 10000000
                choosed_component = None
                
                for _component in components:
                    latitude, longitude = next((warehouse[2], warehouse[3] for warehouse in all_warehouses if warehouse[0] == _component[7]), None)
                    distance = requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": main_warehouse[2],"sender_longitude": main_warehouse[3], "receiver_latitude": latitude,"receiver_longitude": longitude})
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
                requests.put(f"{DB_URL}/component?component_id={choosed_component[0]}&qty={-1*component['qty']}")



            price += _comp[3] * component['qty'] for _comp in components



    #update order price
    requests.put(f"{DB_URL}/order?order_id={orderId.value}&price={price}")










'''
    ordered_components = requests.get(f"{DB_URL}/orderedcomponent?orderId={orderId.value}")
    
    for ordered_component in ordered_components:
        # Check if the component is assembleable
        component = requests.get(f"{DB_URL}/component?prod_id={ordered_component[1]}")
        print(f"ordered_component: {ordered_component.text}")
        #print(f"component: {component.text}")
        component = component.json()
        if not component[4]:
            # Cerca il magazzino più vicino al cliente, si calcola il costo della spedizione
            customer_coordinates = requests.get(f"{GEOLOC_URL}/distance/address?address={int(order['address'])}")
            min_distance = 10000000
            warehouse_id = None
            for warehouse in all_warehouses:
                distance = requests.post(f"{GEOLOC_URL}/distance/calculate", json={"sender_latitude": customer_cordinates[0],"sender_longitude": customer_cordinates[1], "receiver_latitude": warehouse[1],"receiver_longitude": warehouse[2]})
                if distance < min_distance:
                    min_distance = distance
                    warehouse_id = warehouse[0]
            print(f"warehouse_id: {warehouse_id}")
            print(f"min_distance: {min_distance}")

            return {"preventivo": 1000}
    
    # Aggiorna prezzo dell'ordine aggiungendo il costo della spedizione e ritorna il totale
   '''     
    return {"preventivo": 1100}
