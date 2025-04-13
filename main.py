from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SumaInput(BaseModel):
    a: float
    b: float

@app.post("/sumar")
def sumar_numeros(data: SumaInput):
    resultado = data.a + data.b
    print(resultado)
    return {"resultado": resultado}