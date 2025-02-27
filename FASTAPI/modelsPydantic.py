from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id:int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre:str = Field(..., min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    edad: int = Field(..., ge=5, lt=125, description="La edad un numero e igual o mayor que 5 y menor que 125") 
    correo: str = Field(..., description="Debe ser una dirección de correo electrónico válida", 
                        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", example="ejemplo@dominio.com")