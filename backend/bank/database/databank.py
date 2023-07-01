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
        #data  = """INSERT INTO users
        #                  (id, name, amount, username, password)
        #                  VALUES (?, ?, ?, ?, ?);"""

        test = """INSERT INTO users
                          (id, name, amount, username, password) 
                           VALUES 
                          (1,'James',100,'fede','rico')"""

        #data_tuple = (1, name, 100, username, password)
        db.execute(test)
        database.commit()
        return("executed corr")
    except sqlite3.Error as error:
        return("Failed to insert data into sqlite table", error)
    finally:
        #if database:
        #    database.close()
        print("The SQLite connection is closed")


