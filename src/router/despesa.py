from fastapi import APIRouter,HTTPException,status

from schemas.schemas import DespesaInput
from repository.despesa import DespesaRepository

despesa_router=APIRouter(prefix="/despesas")

async def check_date(list_receita,date,description):
    for i in list_receita:
        if i.data.month==date and i.descricao==description:
            return False
    return True

@despesa_router.post("/")
async def create_despesa(despesa_input:DespesaInput):
    if check_date(await DespesaRepository.get_all(),despesa_input.data,despesa_input.descricao)
        return await DespesaRepository.create_despesa(despesa_input)
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)