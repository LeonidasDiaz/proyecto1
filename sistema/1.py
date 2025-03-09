import pandas as pd
import os
ruta_carpeta = "alumnos/"
valor_buscar = 8


# Buscar archivos Excel en la carpeta
archivos_excel = [f for f in os.listdir(ruta_carpeta) if f.endswith(".xlsx")]

if archivos_excel:
    ruta_archivo = os.path.join(ruta_carpeta, archivos_excel[0])  # Toma el primer archivo encontrado

    df = pd.read_excel(ruta_archivo, sheet_name="LC")
    
    print(df.columns)



    filas_encontradas = df[df["Unnamed: 5"] == valor_buscar]

    if not filas_encontradas.empty:
        print("Filas encontradas:")
        print(filas_encontradas)
    else:
        print(f"No se encontraron filas con '{valor_buscar}' .")

else:
    print(f"No se encontraron archivos Excel en la carpeta: {ruta_carpeta}")
