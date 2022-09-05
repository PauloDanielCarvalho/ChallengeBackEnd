from database.connection import async_session
from schemas.schemas import DespesaInput
from models.models import Despesa

from sqlalchemy import delete,update
from sqlalchemy.future import select
class DespesaRepository:
    async def create_despesa(despesa_input:DespesaInput):
        async with async_session() as session:
            async with session.begin():
                despesa=Despesa(descricao=despesa_input.descricao,valor=despesa_input.valor,data=despesa_input.data,categoria=despesa_input.categoria)
                session.add(despesa)
                await session.commit()
                return despesa
    
    async def get_all():
        async with async_session() as session:
            despesas= await session.execute(select(Despesa))
            return despesas.scalars().all()

    async def delete_all():
        async with async_session() as session:
            await session.execute(delete(Despesa))
            await session.commit()
    
    async def get_by_id(id:int):
        async with async_session() as session:
            despesa=await session.execute(select(Despesa).where(Despesa.id==id))
            return despesa.scalars().first()
    
    async def update_by_id(despesa:DespesaInput,id:int):
        async with async_session() as session:
            await session.execute(update(Despesa).where(Despesa.id==id).values(descricao=despesa.descricao,
            valor=despesa.valor,data=despesa.data,categoria=despesa.categoria))
            await session.commit()
    
    async def delete_by_id(id:int):
        async with async_session() as session:
            await session.execute(delete(Despesa).where(Despesa.id==id))
            await session.commit()