from fastapi import FastAPI, HTTPException, Depends
from tokenGen import createToken
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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

#dependencies=[Depends(BaererJWT())] se encarga de verificar si el token es valido

#endpoint Consultar todos
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db= Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Excepcion as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible conectar" , "Excepcion": str(x)})
    finally:
        db.close()

#endpoint Consultar por id
@app.get('/usuario/{id}', tags=['Operaciones CRUD'])
def ConsultaUno(id:int):
    db= Session()
    try:
        consulta= db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta))
    except Excepcion as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible conectar" , "Excepcion": str(x)})
    finally:
        db.close()

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
        return JSONResponse(status_code=500, content={"mensaje": "No se Guardo" , "Excepcion": str(e)})
    finally:
        db.close()
    

""" #endpoint Para modificar usuarios
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
    raise HTTPException(status_code=404, detail="Usuario no encontrado") """