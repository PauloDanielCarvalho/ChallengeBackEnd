from curses import echo
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL="postgresql+asyncpg://admin:admin@database:5432/dbFastapi"

engine=create_async_engine(DATABASE_URL,echo=True)

async_session=sessionmaker(engine,expire_on_commit=False,class_=AsyncSession)