from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from  app.services.cleaning import filtrar_ciudad

# Creamos rutas para Clean Data
router = APIRouter()

# Ruta para la verificación de salud del servicio
@router.get("/clean")
def health_check():
    return {"status": "ok"}

# Ruta para subir un archivo CSV
@router.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):

    # Validamos extension
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos csv")
    
    # Leemos el archivo con pandas
    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer el archivo CSV: {str(e)}")
    
    # Logica
    columnas = df.columns.tolist()
    num_filas = df.shape[0]

    resultado = filtrar_ciudad(df)

    # Retornamos el resultado
    return {
        "columnas": columnas,
        "num_filas": num_filas,
        "resultado": resultado,
        "message": "Archivo CSV procesado correctamente",
    }