from fastapi import FastAPI, HTTPException
from typing import Optional, List
from modelsPydantic import modelUsuario

app= FastAPI(
    title='Mi primer API 196',
    description='Luis Antonio Montoya Magdaleno',
    version='1.0.1'
)

usuarios=[
    {"id":1, "nombre":"luis", "edad":22, "correo":"luis@example.com"},
    {"id":2, "nombre":"antonio", "edad":21, "correo":"antonio@example.com"},
    {"id":3, "nombre":"iochy", "edad":23, "correo":"iochy@example.com"},
    {"id":4, "nombre":"lucy", "edad":18, "correo":"lucy@example.com"},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastAPI': 'LuisAntonioMontoya'}

#endpoint Consultar todos
@app.get('/usuarios', response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endpoint Para agregar usuarios
@app.post('/usuario/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.id:
            raise HTTPException(status_code=400, detail="El id ya esta registrado")
    
    usuarios.append(usuarionuevo)
    return usuarionuevo 

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