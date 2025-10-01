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
def anyadirMed(contador: int, tipo: int, medicion: float):
    try:
        fecha = datetime.utcnow().isoformat()
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute(
            "INSERT INTO datosMedidas (contador, tipo, medicion, fecha) VALUES (?, ?, ?, ?)",
            (contador, tipo, medicion, fecha)
        )
        conn.commit()
        conn.close()
        return {"contador": contador, "tipo": tipo, "medicion": medicion, "fecha": fecha}
    except Exception as e:
        return {"error": str(e)}


#Recuperar última medida
def ultimaMed():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT contador, tipo, medicion, fecha FROM datosMedidas ORDER BY contador DESC LIMIT 1")
    fila = c.fetchone()
    conn.close()
    if fila:
        return {"contador" : fila[0], "tipo" : fila[1], "medicion" : fila[2], "fecha" : fila[3]}
    return None

