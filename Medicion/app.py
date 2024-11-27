from datetime import datetime
import sqlite3
from flask import Flask, request

# Ruta de la base de datos
db_path = 'sensor.sqlite'

# Crear o inicializar la base de datos
conn = sqlite3.connect(db_path)
with open("sensor.sql") as f:
    conn.executescript(f.read())
conn.close()

app = Flask(__name__)
@app.route('/dht11', methods=('POST',))
def registrar_dht11():
    # Obtener los datos enviados desde el sensor
    temperatura = float(request.form['temperatura'])
    humedad = float(request.form['humedad'])
    print(f'Temperatura: {temperatura}°C, Humedad: {humedad}%')

    # Registrar la fecha y hora actuales
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insertar los datos en la base de datos
    conn = sqlite3.connect(db_path)
    conn.execute('''
        INSERT INTO mediciones (timestamp, temperatura, humedad)
        VALUES (?, ?, ?)
    ''', (timestamp, temperatura, humedad))
    conn.commit()
    conn.close()

    return f'Datos registrados: Temperatura: {temperatura}°C, Humedad: {humedad}%'

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
