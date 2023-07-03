import sqlite3
'''create database if not exists'''
path = "bank.db"
database = sqlite3.connect(path)
db = database.cursor()
sql = 'create table if not exists ' + 'users' + ' (id integer PRIMARY KEY, name text NOT NULL, amount real, username text NOT NULL, password text NOT NULL)'
db.execute(sql)
sql = 'create table if not exists ' + 'history' + ' (tx_id integer PRIMARY KEY, sender integer NOT NULL, receiver integer NOT NULL, amount real NOT NULL, FOREIGN KEY(sender) REFERENCES users(id), FOREIGN KEY(receiver) REFERENCES users(id))'
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

'''insert user into database'''
def insert_user(name, username, password):
    try:
        data  = """INSERT INTO users (name, amount, username, password) VALUES (?, ?, ?, ?);"""
        data_tuple = (name, 100, username, password)
        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return(f"{username} created")
    except sqlite3.Error as e:
        return("Failed to create user: ", e)

'''get user amount given user id'''
def get_user_balance(user_id):
    try:
        amount = """SELECT amount FROM users WHERE id=?"""
        connection, cursor = connect(path)        
        fetch_amount = cursor.execute(amount, (user_id, ))
        return fetch_amount.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get user {user_id}")

'''insert transaction into database'''
def insert_tx(sender, receiver, amount):
    try:
        tx = """INSERT INTO history (sender, receiver, amount) VALUES (?, ?, ?);"""
        tx_data = (sender, receiver, amount)
        connection, cursor = connect(path)
        cursor.execute(tx, tx_data)
        connection.commit()
        tx_id = cursor.lastrowid
        return tx_id
    except sqlite3.Error as e:
        return(f"cannot insert transaction")

'''get transaction given transaction id'''
def get_tx(tx_id):
    try:
        tx = """SELECT * FROM history WHERE tx_id=?"""
        connection, cursor = connect(path)
        tx_exec = cursor.execute(tx, (tx_id, ))
        return tx_exec.fetchone()
    except sqlite3.Error as e:
        return(f"cannot get transaction with id: {tx_id}")

'''update balance'''
def update_user_balance(user_id, amount):
    try:
        user_data = """UPDATE users SET amount = amount + ? WHERE id = ?"""
        user_var = (amount, user_id)
        connection, cursor = connect(path)
        cursor.execute(user_data, user_var)
        connection.commit()
        return("balance updated")
    except sqlite3.Error as e:
        return(f"cannot update user balance")

