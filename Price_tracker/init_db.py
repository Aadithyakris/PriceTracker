import sqlite3

#connect to database
conn= sqlite3.connect('tracker.db')

#send commands to db
cursor=conn.cursor()

#create products table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               url TEXT NULL UNIQUE,
               target_price REAL NOT NULL)
               '''
               )

#create price history table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS price_history(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_id INTEGER NOT NULL,
               price REAL NOT NULL,
               timestamp DATETIME DEFAULT CURRENT_TIMESTSMP,
               FOREIGN KEY(product_id) REFERENCES products(id)
               )
               ''')

conn.commit()
conn.close()

print("databse tracker.db initiallized")