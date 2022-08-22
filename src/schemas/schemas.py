
from pydantic import BaseModel
from datetime import date

class ReceitaInput(BaseModel):
    descricao:str
    valor:float
    data:date
    class Config:
        orm_mode = True

class DespesaInput(BaseModel):
    descricao:str
    valor:float
    data:date