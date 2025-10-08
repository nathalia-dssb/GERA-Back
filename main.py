from fastapi import FastAPI
import pandas as pd

df = pd.read_excel("CONCENTRADO_RESGUARDANTES_CON_CLAVE.xlsx")
app = FastAPI()


@app.get("/")#en rutadores 
def root():
    return{"mensaje ": "API para leer datos de resguardantes"}

@app.get("/datos")
def obtener_datos():
    # Reemplaza los valores NaN (vacíos) por texto vacío o None
    return df.fillna("").to_dict(orient="records")

@app.get("/datos/{clave}")
def obtener_dato(clave: str):
    # Usa la tercera columna (índice 2)
    columna_clave = df.columns[2]

    # Reemplaza NaN para evitar errores
    datos = df.fillna("")

    #Filtra por la clave
    fila = datos[datos[columna_clave].astype(str) == str(clave)]

    if not fila.empty:
        return fila.iloc[0].to_dict()
    else:
        return {"Error": f"Clave {clave} no encontrada en la columna '{columna_clave}'"}

@app.get("/datos/{nombre}")
def obtener_datos_por_nombre(nombre: str):
    columna_clave = df.columns[1]
    datos = df.fillna("")
    coincidencias = datos[datos[columna_clave].astype(str).str.lower() == nombre.lower()]

    if not coincidencias.empty:
        return coincidencias.to_dict(orient="records")
    else:
        return {"Error": f"No se encontraron registros con el nombre '{nombre}'"}
