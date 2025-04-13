from fastapi import FastAPI
from app.routes.clean import router as clean_router

# Instancia de fastaApi con titulo y version
app = FastAPI(title="Clean data", version="1.0")

# Incluir rutas de la API   
app.include_router(clean_router)

# Ruta de prueba
app.get("/")
def root():
    return {"message": "Clean data is running"}