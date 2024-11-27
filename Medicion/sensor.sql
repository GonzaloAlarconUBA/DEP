CREATE TABLE IF NOT EXISTS mediciones (
    id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
    temperatura REAL,
    humedad REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);