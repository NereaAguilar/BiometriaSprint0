#---------------------------------
# Nerea Aguilar Fores
#---------------------------------

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
import logica

# Crear aplicacion FastAPI
app = FastAPI()

logica.init_db()

# Modelo de entrada
class Medida(BaseModel):
    contador: int
    tipo: int
    medicion: float

# Modelo de salida
class MedidaOut(Medida):
    fecha: str

# Agregar medida
@app.post("/medida", response_model=MedidaOut)
def nueva_medida(data: Medida):
    return logica.anyadirMed(data.contador, data.tipo, data.medicion)

# Obtener ultima medida
@app.get("/medida/ultima", response_model=MedidaOut)
def ultima_medida():
    ultima = logica.ultimaMed()
    if ultima:
        return ultima
    raise HTTPException(status_code=404, detail="No hay medidas en la base de datos")