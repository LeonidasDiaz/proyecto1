import pandas as pd
import os

ruta_carpeta = "alumnos/"


def hojas(ruta_carpeta):
    # Buscar archivos Excel en la carpeta
    archivos_excel = [f for f in os.listdir(ruta_carpeta) if f.endswith(".xlsx")]

    if archivos_excel:
        ruta_archivo = os.path.join(ruta_carpeta, archivos_excel[0])  # Toma el primer archivo encontrado
        xls = pd.ExcelFile(ruta_archivo)

        hojas = xls.sheet_names
        return hojas

    else:
        print(f"No se encontraron archivos Excel en la carpeta: {ruta_carpeta}")
        return None
    
print(hojas(ruta_carpeta))