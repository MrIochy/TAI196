from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):
    name:str = Field(..., min_length=3, max_length=90, description="Nombre debe contener solo letras y espacios")
    age: int = Field(..., ge=4, lt=125, description="La edad debe ser un numero mayor que 4 y menor que 125") 
    email: str = Field(..., description="Debe ser una dirección de correo electrónico válida", 
                        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", example="ejemplo@dominio.com")

class modelAuth(BaseModel):
    correo:EmailStr
    passw:str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña minimo 8 caracteres")