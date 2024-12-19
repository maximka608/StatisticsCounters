from app.database.engine import make_engine
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker
from app.database.schemas import BaseModel, Statistic
from datetime import date
import asyncio

async def create_table(engine: AsyncEngine) -> None:
    async with engine.connect() as connection:
        await connection.run_sync(lambda conn: BaseModel.metadata.drop_all(conn))
        await connection.run_sync(lambda conn: BaseModel.metadata.create_all(conn))
        await connection.commit()

async def write_records(engine: AsyncEngine) -> None:
    session_factory = async_sessionmaker(engine)
    async with session_factory() as session:
        stat1 = Statistic(date=date(2024,1, 31), views=50, clicks=1, cost=12)
        stat2 = Statistic(date=date(2022, 4,13), views=100, clicks=5, cost=20)
        session.add_all([stat1, stat2])
        await session.commit()

async def main() -> None:
    engine = await make_engine()
    await create_table(engine)
    await write_records(engine)

if __name__ == '__main__':
    asyncio.run(main())
