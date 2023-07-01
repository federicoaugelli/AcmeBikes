import sqlite3

database = sqlite3.connect("bank.db")
db = database.cursor()

sql = 'create table if not exists ' + 'users' + ' (id integer PRIMARY KEY, name text NOT NULL, amount real, username text NOT NULL, password text NOT NULL)'
db.execute(sql)

sql = 'create table if not exists ' + 'history' + ' (tx_id integer, sender integer NOT NULL, receiver integer NOT NULL, detail text, amount real NOT NULL, FOREIGN KEY(sender) REFERENCES users(id), FOREIGN KEY(receiver) REFERENCES users(id))'
db.execute(sql)
database.commit()

def register(name, username, password):
    try:
        database = sqlite3.connect("bank.db")
        db = database.cursor()
        data  = """INSERT INTO users
                          (name, amount, username, password)
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (name, 100, username, password)
        db.execute(data, data_tuple)
        database.commit()
        return("executed corr")
    except sqlite3.Error as error:
        return("Failed to insert data into sqlite table", error)
    finally:
        if database:
            database.close()
        print("The SQLite connection is closed")


