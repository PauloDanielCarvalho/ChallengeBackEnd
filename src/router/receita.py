from fastapi import APIRouter,HTTPException,status
from repository.receita import ReceitaRepository
from schemas.schemas import ReceitaInput
from typing import List


receita_router=APIRouter(prefix="/receita")

async def check_date(list_receita,date,description):
    for i in list_receita:
        if i.data.month==date and i.descricao==description:
            return False
    return True

@receita_router.post("/cadastro",response_model=ReceitaInput)
async def cadastro_receita(receita_input:ReceitaInput):
    list_receitas = await ReceitaRepository.get_receitas()
    if await check_date(list_receitas,receita_input.data.month,receita_input.descricao):
        receita = await ReceitaRepository.create_receita(receita_input)
        return receita
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)

@receita_router.get("/list_reiceitas",response_model=List[ReceitaInput])
async def list_receitas():
    try:
        list_receitas=await ReceitaRepository.get_receitas()
        return list_receitas
    except Exception as erroo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(erroo))

@receita_router.get("/",response_model=ReceitaInput)
async def get_by_id(id:int):
    try:
        return await ReceitaRepository.get_by_id(id)
    except Exception as erroo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(erroo))

@receita_router.delete("/")
async def delete_all():
    await ReceitaRepository.delete_all()
   
    
   


