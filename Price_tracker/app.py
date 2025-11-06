import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#get databse connection
def get_db_connection():
    conn =  sqlite3.connect('tracker.db')
    conn.row_factory=sqlite3.Row
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        target_price = request.form['target_price']
        #save data to db
        conn = get_db_connection()
        conn.execute('INSERT INTO products (name, url, target_price) VALUES (?, ?, ?)', (name, url, target_price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn = get_db_connection() #connect to db
    products = conn.execute('SELECT * FROM products').fetchall() #fetch all products from products table
    conn.close()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
