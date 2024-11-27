from serial import Serial
import sqlite3
import json
from datetime import datetime

# Configuración del puerto serie
ser = Serial('/dev/ttyACM0', 9600)  # Cambia 'COM3' por tu puerto serie
conn = sqlite3.connect('sensores.db')
cursor = conn.cursor()

# Asegurarse de que la tabla exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS mediciones (
    id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
    temperatura REAL,
    humedad REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

while True:
    try:
        # Leer línea del puerto serie
        line = ser.readline().decode('utf-8').strip()
        data = json.loads(line)  # Parsear JSON

        # Insertar datos en la base de datos
        temperatura = data['temperatura']
        humedad = data['humedad']
        cursor.execute("INSERT INTO mediciones (temperatura, humedad) VALUES (?, ?)", (temperatura, humedad))
        conn.commit()

        print(f"Insertado: Temperatura={temperatura}°C, Humedad={humedad}% a las {datetime.now()}")

    except (ValueError, json.JSONDecodeError):
        print("Dato inválido recibido")