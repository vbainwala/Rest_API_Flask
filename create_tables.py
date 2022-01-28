import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)


create_table = "CREATE TABLE items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

#cursor.execute("INSERT INTO items values ('test', 10.99)")

connection.commit()

connection.close()
