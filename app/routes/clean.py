from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import pandas as pd

# Creamos rutas para Clean Data
router = APIRouter()

# Directorio donde se guardarán los archivos CSV subidos (opcional)
UPLOAD_DIR = "csv_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

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

    # Retornamos el resultado
    return {
        "columnas": columnas,
        "num_filas": num_filas,
        "message": "Archivo CSV procesado correctamente",
    }