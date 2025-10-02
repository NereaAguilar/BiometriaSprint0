#---------------------------------
# Nerea Aguilar Fores
#---------------------------------

import sqlite3
from datetime import datetime

DB = "datos.db"

#Inicializar base de datos
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS datosMedidas (
            contador INTEGER PRIMARY KEY,
            tipo INTEGER,
            medicion REAL,
            fecha TEXT
        )
    """)
    conn.commit()
    conn.close()

#Añadir medidas
def anyadirMed(tipo: int, medicion: float):
    fecha = datetime.utcnow().isoformat()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO datosMedidas (tipo, medicion, fecha) VALUES (?, ?, ?)",
              (tipo, medicion, fecha))
    conn.commit()
    conn.close()
    return {"id": c.lastrowid, "tipo": tipo, "medicion": medicion, "fecha": fecha}



#Recuperar última medida
def ultimaMed():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, tipo, medicion, fecha FROM datosMedidas ORDER BY id DESC LIMIT 1")
    fila = c.fetchone()
    conn.close()
    if fila:
        return {"id": fila[0], "tipo": fila[1], "medicion": fila[2], "fecha": fila[3]}
    return None