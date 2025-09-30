import sqlite3

#Abrir/crear base de datos
conn = sqlite3.connect("datos.db")
cur = conn.cursor()

print("Conexión OK")

#Crear tabla(si no existe)
cur.execute("""
CREATE TABLE IF NOT EXISTS datosMedidas(
            contador INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo INTEGER NOT NULL,
            medicion REAL NOT NULL,
            fecha TEXT DEFAULT (datetime('now','localtime'))
    );
""")

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tablas:", cur.fetchall())

# Prueba
# Insertar un dato
#cur.execute("INSERT INTO datosMedidas (tipo, medicion) VALUES (?, ?)", (11, 240))

# Consultar todos los registros
#cur.execute("SELECT * FROM datosMedidas")
#print("Datos:", cur.fetchall())

#Guardar cambios y cerrar conexion
conn.commit()
conn.close()

print("Base lista")