from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from modelsPydantic import modelEnvio

app= FastAPI(
    title='Examen2doP',
    version='1.0.1'
)

class modelEnvio(BaseModel):
    cp:str
    destino:str
    peso:int

envios=[
    {"cp":"11111", "destino":"destino1", "peso":50},
    {"cp":"22222", "destino":"destino2", "peso":30},
    {"cp":"33333", "destino":"destino3", "peso":100},
    {"cp":"44444", "destino":"destino4", "peso":10},
    {"cp":"55555", "destino":"destino5", "peso":70},
    {"cp":"66666", "destino":"destino6", "peso":20},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola Examen': 'LuisAntonioMontoya'}

#endpoint Para eliminar 1 envio por codigo postal
@app.delete('/envios/{cp}', tags=['Operaciones CRUD'])
def Eliminar(cp: str):
    for index, codigopostal in enumerate(envios):
        if codigopostal["cp"] == cp:
            del envios[index]
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#endpoint para mostrar todos los envios
@app.get('/envios', response_model=List[modelEnvio], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return envios