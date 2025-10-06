#---------------------------------
# Nerea Aguilar Fores
#---------------------------------

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
import logica

from fastapi.staticfiles import StaticFiles
import os

# Crear aplicacion FastAPI
app = FastAPI()

logica.init_db()

# Modelo de entrada
class Medida(BaseModel):
    tipo: int
    medicion: float

# Modelo de salida
class MedidaOut(Medida):
    id: int
    fecha: str

# Agregar medida
@app.post("/medida", response_model=MedidaOut)
def nueva_medida(data: Medida):
    return logica.anyadirMed(data.tipo, data.medicion)

# Obtener ultima medida
@app.get("/medida/ultima", response_model=MedidaOut)
def ultima_medida():
    ultima = logica.ultimaMed()
    if ultima:
        return ultima
    raise HTTPException(status_code=404, detail="No hay medidas en la base de datos")

# Path a la web
web_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "web"))
app.mount("/web", StaticFiles(directory=web_dir, html=True), name="web")

# Permitir ejecutar directamente con python app.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
