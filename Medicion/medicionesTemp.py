from datetime import datetime
import sqlite3
from flask import Flask, request

db_path = 'sensor.sqlite'
conn = sqlite3.connect(db_path)

with open("sensor.sql") as f:
    conn.executescript(f.read())
app = Flask(__name__)
@app.route('/luz', methods=('POST',))
def hello():
    luz = float(request.form['sensor'])
    print(f'Sensor Luz: {luz}')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect(db_path)
    conn.execute('''
                        INSERT INTO LuzData (timestamp, luz)
                        VALUES (?, ?)
                    ''', (timestamp, luz))
    conn.commit()    
    conn.close()
    return f'Sensor Luz: {luz}'