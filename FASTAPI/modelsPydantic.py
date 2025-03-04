from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):
    id:int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre:str = Field(..., min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    edad: int = Field(..., ge=5, lt=125, description="La edad un numero e igual o mayor que 5 y menor que 125") 
    correo: str = Field(..., description="Debe ser una dirección de correo electrónico válida", 
                        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", example="ejemplo@dominio.com")

class modelAuth(BaseModel):
    correo:EmailStr
    passw:str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña minimo 8 caracteres")