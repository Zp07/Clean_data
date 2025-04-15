import os
import pandas as pd
from datetime import datetime

# Funcion para filtrar el DataFrame
def filtrar_ciudad(df: pd.DataFrame, output_dir: str = "datasets"):
    # Verificar si el DataFrame está vacío
    os.makedirs(output_dir, exist_ok=True)

    # Obtener la fecha actual en formato YYYY-MM-DD
    fecha_actual = datetime.today().strftime('%Y-%m-%d')

    # Obtener la lista de ciudades únicas
    ciudades = df["city"].unique()
    resultado = []

    # Separar el DataFrame
    for ciudad in ciudades:
        # Filtrar el DataFrame por ciudad
        df_ciudad = df[df["city"] == ciudad]
        dir_ciudad = os.path.join(output_dir, ciudad)
        
        # Verificar existencia de directorio ciudad, si no  lo crea
        os.makedirs(dir_ciudad, exist_ok=True)

        # Guardar el DataFrame filtrado en un archivo CSV
        archivo_salida = os.path.join(dir_ciudad, f"ciudad_{ciudad}_{fecha_actual}.csv")
        df_ciudad.to_csv(archivo_salida, index=False)
        resultado.append({"ciudad": ciudad, "filas":len(df_ciudad)})

    # retorna el diccionario de ciudades y filas
    return {
        "mensaje" : "separación por ciudad completada",
        "total_ciudades" : len(ciudades),
        "resultado" : resultado,

    }

    
