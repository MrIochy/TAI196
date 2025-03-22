from pydantic import BaseModel, Field

class modelEnvio(BaseModel):
    cp:str = Field(..., min_length=5, description="Codigo postal debe contener mas de 5 numeros")
    destino:str = Field(..., min_length=6, description="Destino debe contener minimo 6, contiene tanto letras numeros y espacios")
    peso:int = Field(..., gt=0, lt=500, description="La edad un numero e igual o mayor que 5 y menor que 125") 