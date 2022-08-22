from database.connection import async_session
from schemas.schemas import DespesaInput
from models.models import Despesa

from sqlalchemy.future import select
class DespesaRepository:
    async def create_despesa(despesa_input:DespesaInput):
        async with async_session() as session:
            async with session.begin():
                despesa=Despesa(descricao=despesa_input.descricao,valor=despesa_input.valor,data=despesa_input.data)
                await session.add(despesa)
                await session.commit()
                return despesa
    
    async def get_all():
        async with async_session() as session:
            despesas= await session.execute(select(Despesa))
            return despesas.scalars().all()