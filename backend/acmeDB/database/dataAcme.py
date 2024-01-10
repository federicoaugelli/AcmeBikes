import sqlite3
'''create database if not exists'''
path = "acmedb.db"
database = sqlite3.connect(path)
db = database.cursor()
sql = 'create table if not exists ' + 'warehouse' + ' (id integer PRIMARY KEY, name text NOT NULL, address text NOT NULL, latitude real NOT NULL, longitude real NOT NULL)'
db.execute(sql)
sql = 'create table if not exists ' + 'component' + """ (id integer PRIMARY KEY, 
                                                       productId integer NOT NULL,
                                                       name text NOT NULL,
                                                       price integer NOT NULL,
                                                       assembleable integer,
                                                       qty integer,
                                                       type text,
                                                       location integer NOT NULL,
                                                       FOREIGN KEY(location) REFERENCES warehouse(id)) """
db.execute(sql)
sql = 'create table if not exists ' + 'bikes' + """ (id integer PRIMARY KEY, 
                                                  productId integer NOT NULL,
                                                  name text NOT NULL,
                                                  price integer NOT NULL,
                                                  qty integer,
                                                  color text NOT NULL,
                                                  location integer NOT NULL,
                                                  FOREIGN KEY(location) REFERENCES warehouse(id)) """
db.execute(sql)
sql = 'create table if not exists ' + 'customisation'+ """ (id integer PRIMARY KEY,
                                                      bike_id integer NOT NULL,
                                                      component_id integer NOT NULL,
                                                      FOREIGN KEY(bike_id) REFERENCES bikes(id),
                                                      FOREIGN KEY(component_id) REFERENCES component(id)) """
db.execute(sql)
sql = 'create table if not exists ' + 'orders' + """ (id integer PRIMARY KEY,
                                                    price real,
                                                    customer text NOT NULL, 
                                                    address text NOT NULL, 
                                                    shipment real) """
db.execute(sql)
sql = 'create table if not exists ' + 'orderedComponents' + """ (id integer PRIMARY KEY, 
                                                               component_id integer,
                                                               bike_id integer,
                                                               name text NOT NULL,
                                                               qty integer,
                                                               orderId integer NOT NULL,
                                                               FOREIGN KEY(bike_id) REFERENCES bike(id),
                                                               FOREIGN KEY(component_id) REFERENCES component(id),
                                                               FOREIGN KEY(orderId) REFERENCES orders(id)) """
db.execute(sql)
database.commit()

'''connect to database'''
def connect(db):
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
    except sqlite3.Error as e:
        return None, e
    return connection, cursor

def get_all_warehouses():
    try:
        user_query = """SELECT id, latitude, longitude FROM warehouse"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query)
        return user_query_exec.fetchall()
    except sqlite3.Error as e:
        return(f"cannot get: warehouses")

#warehouse
def get_warehouse(warehouseId):
    try:
        user_query = """SELECT * FROM warehouse WHERE id=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (warehouseId, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get: {name}")

def create_warehouse(name, address, latitude, longitude):
    try:
        data  = """INSERT INTO warehouse (name, address, latitude, longitude) VALUES (?, ?, ?, ?);"""
        data_tuple = (name, address, latitude, longitude)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} created")
    except sqlite3.Error as e:
        return("Failed to create user: ", e)

def delete_warehouse(warehouseId):
    try:
        data = """DELETE FROM warehouse WHERE id = ?"""
        data_tuple = (warehouseId, )
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"deleted successfully.")
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")

#order
def insert_order(price, customer, address, shipment):
    try:
        data  = """INSERT INTO orders (price, customer, address, shipment) VALUES (?, ?, ?, ?);"""
        data_tuple = (price, customer, address, shipment)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        return("Failed to create order: ", e)


def get_order(order_id):
    try:
        user_query = """SELECT * FROM orders WHERE id=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (order_id, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get: {order_id}")

def modify_order(order_id, price):
    try:
        data = """UPDATE orders SET price=price+? WHERE id=?"""
        data_var = (price, order_id)
        connection, cursor = connect(path)
        cursor.execute(data, data_var)
        connection.commit()
        return(f"order modified")
    except sqlite3.Error as e:
        return("Failed to modify order: ", e)

def add_shipment(order_id, shipment_price):
    try:
        data = """UPDATE orders SET shipment=+? WHERE id=?"""
        data_var = (shipment_price, order_id)
        connection, cursor = connect(path)
        cursor.execute(data, data_var)
        connection.commit()
        return(f"shipment added")
    except sqlite3.Error as e:
        return("Failed to add shipment: ", e)

#rilasciare pezzi
def cancel_order(order_id):
    try:
        data = """DELETE FROM orders WHERE id = ?"""
        data_tuple = (order_id, )
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"Order {order_id} deleted successfully.")
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")

def apply_discount(order_id, perc):
    try:
        data = """UPDATE orders SET price=price-(price*?/100) WHERE id=?"""
        data_var = (perc, order_id)
        connection, cursor = connect(path)
        cursor.execute(data, data_var)
        connection.commit()
        return(f"discount applied")
    except sqlite3.Error as e:
        return("Failed to apply discount: ", e)


#ordered components
def insert_ordered_component(componentId, bikeId, name, qty, orderId):
    try:
        data  = """INSERT INTO orderedComponents (component_id, bike_id, name, qty, orderId) VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (componentId, bikeId, name, qty, orderId, )
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} blocked")
    except sqlite3.Error as e:
        return("Failed to create user: ", e)

def get_ordered_component(orderId):
    try:
        user_query = """SELECT * FROM orderedComponents WHERE orderId=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (orderId, ))
        return user_query_exec.fetchall()
    except sqlite3.Error as e:
        return(f"cannot get: {orderId}")

def cancel_ordered_component(ordId):
    try:
        data = """DELETE FROM orderedComponents WHERE orderId = ?"""
        data_tuple = (ordId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Entry with id {ordId} deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


#components
def insert_component(productId, name, price, assembleable, qty, ty, location):
    try:
        data  = """INSERT INTO component (productId, name, price, assembleable, qty, type, location) VALUES (?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (productId, name, price, assembleable, qty, ty, location)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} created")
    except sqlite3.Error as e:
        return("Failed to create component: ", e)

def cancel_component(componentId):
    try:
        data = """DELETE FROM component WHERE id = ?"""
        data_tuple = (componentId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Entry with id {entry_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_component(prodId):
    try:
        user_query = """SELECT * FROM component WHERE productId=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (prodId, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get: {productId}")

def modify_component(prod_id, qty):
    try:
        data = """UPDATE component SET qty=? WHERE id=?"""
        data_var = (qty, prod_id)
        connection, cursor = connect(path)
        cursor.execute(data, data_var)
        connection.commit()
        if qty>0:
            return(f"now: {qty} components")
        else:
            return(f"deleted {qty} components")
    except sqlite3.Error as e:
        return("Failed to update quantity: ", e)
        

#bikes
def insert_bike(productId, name, price, qty, color, location):
    try:
        data  = """INSERT INTO bikes (productId, name, price, qty, color, location) VALUES (?, ?, ?, ?, ?, ?);"""
        data_tuple = (productId, name, price, qty, color, location)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} created")
    except sqlite3.Error as e:
        return("Failed to create component: ", e)

def cancel_bike(componentId):
    try:
        data = """DELETE FROM bikes WHERE id = ?"""
        data_tuple = (componentId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Entry deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_bike(prodId):
    try:
        user_query = """SELECT * FROM bikes WHERE productId=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (prodId, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get")

def modify_bike(prod_id, qty):
    try:
        data = """UPDATE bikes SET qty=? WHERE id=?"""
        data_var = (qty, prod_id)
        connection, cursor = connect(path)
        cursor.execute(data, data_var)
        connection.commit()
        if qty>0:
            return(f"now: {qty} components")
        else:
            return(f"deleted {qty} components")
    except sqlite3.Error as e:
        return("Failed to update quantity: ", e)



#customisations
def insert_cust(bikeId, componentId):
    try:
        data  = """INSERT INTO customisation (bike_id, component_id) VALUES (?, ?);"""
        data_tuple = (bikeId, componentId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"customisation created")
    except sqlite3.Error as e:
        return("Failed to create component: ", e)
        
def cancel_cust(bikeId, componentId):
    try:
        data = """DELETE FROM customisation WHERE bike_id = ? AND component_id = ?"""
        data_tuple = (bikeId, componentId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Entry with id deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_cust(bikeId, componentId):
    try:
        user_query ="""SELECT * FROM customisation WHERE bike_id = ? AND component_id = ?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (bikeId, componentId, ))
        isCust = user_query_exec.fetchone()
        if isCust:
            return True
        else:
            return False
    except sqlite3.Error as e:
        return(f"cannot get")




