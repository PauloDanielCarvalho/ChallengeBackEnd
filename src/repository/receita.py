from schemas.schemas import ReceitaInput
from database.connection import async_session
from models.models import Receita

from sqlalchemy.future import select
from sqlalchemy import delete

class ReceitaRepository:
    async def create_receita(receita_input:ReceitaInput):
        async with async_session() as session:
            async with session.begin():
                receita=Receita(descricao=receita_input.descricao,valor=receita_input.valor,data=receita_input.data)
                session.add(receita)
                await session.commit()
                return receita
        
    async def get_receitas():
        async with async_session() as session:
            receitas=await session.execute(select(Receita))
            return receitas.scalars().all()
    
    async def get_by_id(id):
        async with async_session() as session:
            receita=await session.execute(select(Receita).where(Receita.id==id))
            return receita.scalars().first()
    
    async def delete_all():
        async with async_session() as session:
            await session.execute(delete(Receita))
            await session.commit()
