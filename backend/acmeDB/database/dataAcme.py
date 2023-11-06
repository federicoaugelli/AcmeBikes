import sqlite3
'''create database if not exists'''
path = "acmedb.db"
database = sqlite3.connect(path)
db = database.cursor()
sql = 'create table if not exists ' + 'warehouse' + ' (id integer PRIMARY KEY, name text NOT NULL, address text NOT NULL)'
db.execute(sql)
sql = 'create table if not exists ' + 'component' + ' (id integer PRIMARY KEY, productId integer NOT NULL, name text NOT NULL, assembleable integer, qty integer, bookedQty integer,  location integer NOT NULL, FOREIGN KEY(location) REFERENCES warehouse(id))'
db.execute(sql)
sql = 'create table if not exists ' + 'orders' + ' (id integer PRIMARY KEY, price real, customer text NOT NULL, address text NOT NULL)'
db.execute(sql)
sql = 'create table if not exists ' + 'orderedComponents' + ' (id integer PRIMARY KEY, productId integer NOT NULL, name text NOT NULL, qty integer, orderId integer NOT NULL, FOREIGN KEY(productId) REFERENCES component(id), FOREIGN KEY(orderId) REFERENCES orders(id))'
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

#crea magazzino
def create_warehouse(name, address):
    try:
        data  = """INSERT INTO warehouse (name, address) VALUES (?, ?);"""
        data_tuple = (name, address)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} created")
    except sqlite3.Error as e:
        return("Failed to create user: ", e)

#elimina magazzino
def delete_warehouse(warehouseId):
    try:
        data = """DELETE FROM warehouse WHERE id = ?"""
        data_tuple = (warehouseId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Entry with id {entry_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#inserisci ordine in db
def insert_order(price, customer, address):
    try:
        data  = """INSERT INTO orders (price, customer, address) VALUES (?, ?, ?);"""
        data_tuple = (price, customer, address)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"new order created")
    except sqlite3.Error as e:
        return("Failed to create order: ", e)


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

#cancella ordine
def cancel_order(orderid):
    try:
        data = """DELETE FROM orders WHERE id = ?"""
        data_tuple = (orderId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Order {order_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


#inserisci componenti gia ordinati
def insert_ordered_component(productId, name, qty, orderId):
    try:
        data  = """INSERT INTO orderedComponents (productId, name, qty, orderId) VALUES (?, ?, ?, ?);"""
        data_tuple = (productId, name, qty, orderId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} blocked")
    except sqlite3.Error as e:
        return("Failed to create user: ", e)


#togli componenti da componenti ordinati
def cancel_ordered_component(ordId):
    try:
        data = """DELETE FROM orderedComponents WHERE id = ?"""
        data_tuple = (ordId)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        print(f"Entry with id {entry_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


#inserisci nuovi elementi nel db
def insert_component(productId, name, assembleable, qty, bookedQty, location):
    try:
        data  = """INSERT INTO component (productId, name, assembleable, qty, bookedQty, location) VALUES (?, ?, ?, ?, ?, ?);"""
        data_tuple = (productId, name, assembleable, qty, bookedQty, location)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{name} created")
    except sqlite3.Error as e:
        return("Failed to create component: ", e)


#cancella elementi dal db
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

def get_warehouse(warehouseId):
    try:
        user_query = """SELECT * FROM warehouse WHERE id=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (warehouseId, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get: {name}")

def get_order(price, customer, address):
    try:
        user_query = """SELECT * FROM orders WHERE customer=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (price, customer, address, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get: {address}")

def get_ordered_component(productId):
    try:
        user_query = """SELECT * FROM orderedComponents WHERE productId=?"""
        connection, cursor = connect(path)
        user_query_exec = cursor.execute(user_query, (productId, ))
        return user_query_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get: {productId}")



