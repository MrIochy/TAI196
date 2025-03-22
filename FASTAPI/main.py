from fastapi import FastAPI, HTTPException, Depends
from tokenGen import createToken
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from fastapi.responses import JSONResponse
from middlewares import BaererJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app= FastAPI(
    title='Mi primer API 196',
    description='Luis Antonio Montoya Magdaleno',
    version='1.0.1'
)

#levanta las tablas definidas en modelos
Base.metadata.create_all(bind=engine)

usuarios=[
    {"id":1, "nombre":"luis", "edad":22, "correo":"luis@example.com"},
    {"id":2, "nombre":"antonio", "edad":21, "correo":"antonio@example.com"},
    {"id":3, "nombre":"iochy", "edad":23, "correo":"iochy@example.com"},
    {"id":4, "nombre":"lucy", "edad":18, "correo":"lucy@example.com"},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastAPI': 'LuisAntonioMontoya'}

@app.post('/auth', tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == "123@example.com" and autorizado.passw == "123456789":
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"Aviso": "Usario no Autorizado"}

#endpoint Consultar todos
@app.get('/usuarios', dependencies=[Depends(BaererJWT())], response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endpoint Para agregar usuarios
@app.post('/usuario/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario):
    db= Session()
    try:
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje": "Usuario Guardado", "usuario": usuarionuevo.model_dump()})
    except:
        db.rollback()
        return JSONResponse(status_code=599, content={"mensaje": "No se Guardo" , "Excepcion": str(e)})
    finally:
        db.close()
    

#endpoint Para modificar usuarios
@app.put('/usuario/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def Actualizar(id: int, usuarioActualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]

    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#endpoint Para eliminar usuarios
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def Eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")