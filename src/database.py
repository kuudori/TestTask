from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

engine = create_async_engine(settings.DATABASE_URL)
async_session = sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)


async def get_db():
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()


Base = declarative_base()
