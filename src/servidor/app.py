from fastapi import FastAPI

# Creamos la aplicación FastAPI
app = FastAPI()

# Endpoint de prueba
@app.get("/health")
def health():
    return {"status": "ok"}
