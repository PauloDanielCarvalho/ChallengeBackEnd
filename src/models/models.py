from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Float,Date


Base=declarative_base()

class Receita(Base):
    __tablename__="Receitas"
    id=Column(Integer, primary_key=True, autoincrement=True)
    descricao=Column(String)
    valor=Column(Float)
    data=Column(Date)

class Despesa(Base):
    __tablename__="Despesas"
    id=Column(Integer, primary_key=True, autoincrement=True)
    descricao=Column(String)
    valor=Column(Float)
    data=Column(Date)