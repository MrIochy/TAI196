from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title='Mi primer API 196',
    description='Luis Antonio Montoya Magdaleno',
    version='1.0.1'
)

usuarios=[
    {"id":1, "nombre":"luis", "edad":22},
    {"id":2, "nombre":"antonio", "edad":21},
    {"id":3, "nombre":"iochy", "edad":23},
    {"id":4, "nombre":"lucy", "edad":18},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastAPI': 'LuisAntonioMontoya'}

@app.get('/promedio', tags=['Mi Calificacion TAI'])
def promedio():
    return 65.2

#endPoint Parametro Obligatorio
@app.get('/usuario/{id}', tags=['Parametro Obligatorio'])
def consultaUsuario(id:int):
    # connectamos a BD
    # Hacemos consulta retornamos resultset
    return{"Se encontro el usuario": id}

#endPoint Parametro Opcional
@app.get('/usuariox/', tags=['Parametro Opcional'])
def consultaUsuario2(id :Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"mensaje":"Usuario encontrado", "usuario":usuario}
        return {"mensaje":f"No se encontro el id: {id}"}
    else:
        return {"mensaje":"No se proporciono un Id"}
    
# --------------------------------------------------------------------
#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
    # --------------------------------------------------------------------