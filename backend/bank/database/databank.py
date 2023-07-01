import sqlite3
path = "/database/bank.db"

database = sqlite3.connect(oath)
db = database.cursor()

sql = 'create table if not exists ' + 'users' + ' (id integer PRIMARY KEY, name text NOT NULL, amount real, username text NOT NULL, password text NOT NULL)'
db.execute(sql)

sql = 'create table if not exists ' + 'history' + ' (tx_id integer, sender integer NOT NULL, receiver integer NOT NULL, amount real NOT NULL, FOREIGN KEY(sender) REFERENCES users(id), FOREIGN KEY(receiver) REFERENCES users(id))'
db.execute(sql)
database.commit()

def connect(db):
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
    except sqlite3.Error as e:
        return None, e
    return connection, cursor

def register(name, username, password):
    try:
        data  = """INSERT INTO users
                          (name, amount, username, password)
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (name, 100, username, password)

        connection, cursor = connect(path)
        cursor.execute(data, data_tuple)
        connection.commit()
        return("user successfull registered")
    except sqlite3.Error as e:
        return("Failed to insert data", e)

def pay(sender, receiver, amount):
    try:
        connection, cursor = connect(path)
        s_amount = """SELECT amount FROM users WHERE id=?"""
        
        cursor.execute(s_amount, sender)
        sender_amount = cursor.fetchall()

        if not sender_amount >= amount:
            return None

        decrease_sender_amount = """UPDATE users SET amount = amount - ? WHERE id = ?"""
        decrease_data = (ampunt, sender)
        cursor.execute(decrease_sender_amount, decrease_data)

        increase_receiver_amount = """UPDATE users SET amount = amount + ? WHERE id = ? """
        increase_data = (amount, receiver)
        cursor.execute(increase_receiver_amount, increase_data)

        tx = """INSERT INTO history (sender, receiver, amount) VALUES (?, ?, ?);"""
        tx_data = (sender, receiver, amount)
        cursor.execute(tx, tx_data)

        tx_id = cursor.lastrowid

        connection.commit()

        return(f"tx id: {tx_id}")
    except sqlite3.Error as e:
        return(str(e))


def verify_token(tx_id, amount):
    try.

    except sqlite3.Error as e



