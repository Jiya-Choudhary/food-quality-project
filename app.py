import sqlite3
from flask import Flask

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
    insert_data("burger.jpg", "Burnt", "High")
    return "Data inserted!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    