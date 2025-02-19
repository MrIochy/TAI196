from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(
    title="Repaso FastAPI: API de Gestión de Tareas (To-Do List)",
    description="Luis Antonio Montoya Magdaleno",
    version="1.0.1"
)

tareas = [
    {"id":1, "titulo":"Practica 1", "descripcion":"Conocer que es FASTAPI y preparar el entrono para el trabajo con el framework", 
        "vencimiento":"14-02-24", "estado":"completada"},
    {"id":2, "titulo":"Practica 2", "descripcion":"Conocer y trabajar con los Verbos y respuestas HTTP", 
        "vencimiento":"15-02-24", "estado":"no completada"},
    {"id":3, "titulo":"Examen 1er Parcial", "descripcion":"Resolver el examen en Google Forms",
        "vencimiento":"16-02-24", "estado":"no completada"}
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastAPI': 'LuisAntonioMontoya'}

# Endpoint: Obtener todas las tareas
@app.get("/tareas", tags=["Operaciones CRUD"])
def obtener_todas_las_tareas():
    return {"Tareas Registradas": tareas}

# Endpoint: Obtener una tarea específica por su ID
@app.get("/tarea/{id}", tags=["Operaciones CRUD"])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Endpoint: Crear una nueva tarea
@app.post('/tarea/', tags=['Operaciones CRUD'])
def crear_tarea(tarea_nueva: dict):
    for tarea in tareas:
        if tarea["id"] == tarea_nueva.get("id"):
            raise HTTPException(status_code=400, detail="El id ya esta registrado")
    
    tareas.append(tarea_nueva)
    return tarea_nueva 

"""
{"id":4, "titulo":"Examen 2do Parcial", "descripcion":"Resolver el examen en Google Forms", "vencimiento":"16-03-24", "estado":"no completada"}
"""

# Endpoint: Actualizar una tarea existente
@app.put('/tarea/{id}', tags=['Operaciones CRUD'])
def actualizar_tarea(id: int, tarea_actualizada: dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[index].update(tarea_actualizada)
            return tareas[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")