from settings import Postgres
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

DATABASE_URL = f'postgresql+asyncpg://{Postgres.user}:{Postgres.password}@{Postgres.host}:{Postgres.port}/{Postgres.database}'
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

metadata = sqlalchemy.MetaData()
Base = declarative_base()
