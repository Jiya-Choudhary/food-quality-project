import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT,
            prediction TEXT,
            risk TEXT
        )
    ''')
    conn.commit() 
    conn.close()
def insert_data(image_name, prediction, risk):
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO results (image_name, prediction, risk)
        VALUES (?, ?, ?)
    ''', (image_name, prediction, risk))

    conn.commit()
    conn.close()

@app.route('/')
def home():
    if request.method == 'POST':
        file = request.files['file']

        if file:
            filename = file.filename

            # Dummy prediction (temporary)
            prediction = "Burnt"
            risk = "High"

            insert_data(filename, prediction, risk)

            return render_template('index.html', result=prediction, risk=risk)

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    