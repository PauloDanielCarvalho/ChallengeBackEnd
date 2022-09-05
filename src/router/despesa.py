from fastapi import APIRouter,HTTPException,status
from typing import List

from schemas.schemas import DespesaInput
from repository.despesa import DespesaRepository
from router.functions import check_date

despesa_router=APIRouter(prefix="/despesas")

@despesa_router.post("/")
async def create_despesa(despesa_input:DespesaInput):
    lista_despesa=await DespesaRepository.get_all()
    
    if await check_date(lista_despesa,despesa_input.data.month,despesa_input.descricao):
        if despesa_input.categoria == None:
            despesa_input.categoria= "Outras"
        return await DespesaRepository.create_despesa(despesa_input)
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail= "n aceita")

@despesa_router.get("/list_despesa",response_model=List[DespesaInput])
async def list_despesas():
    try:
        list_despesas = await DespesaRepository.get_all()
        return list_despesas
    except Exception as erroo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(erroo))


@despesa_router.delete("/")
async def delete_all():
    await DespesaRepository.delete_all()

@despesa_router.get("/{id}",response_model=DespesaInput)
async def get_by_id(id:int):
    despesa = await DespesaRepository.get_by_id(id)
    return despesa

@despesa_router.put("/",status_code=status.HTTP_200_OK,description="accepted")
async def update_by_id(id:int,despesa:DespesaInput):
    await DespesaRepository.update_by_id(despesa,id)

@despesa_router.delete("/{id}")
async def delete_by_id(id:int):
    await DespesaRepository.delete_by_id(id)