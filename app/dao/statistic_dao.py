from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import and_, select, delete
from app.models.statistic import Statistic
from typing import Any, List
from datetime import date

class StatisticDAO:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self.session = session

    async def add_statistic(self, date: date, views: int, clicks: int, cost: float) -> None:
        query = (
            select(Statistic)
            .select_from(Statistic)
            .where(Statistic.date == date)
        )
        async with self.session() as session:
            result = await session.execute(query)
            record = result.one_or_none()
            if record != None:
                record[0].views += views
                record[0].clicks += clicks
                record[0].cost += cost
            else:
                statistic_obj = Statistic(date=date, views=views, clicks=clicks, cost=cost)
                session.add(statistic_obj)
            await session.commit()

    async def get_statistics(self, date_from: date, date_to: date) -> List[Any]:
        async with self.session() as session:
            query = (
                select(Statistic.date).select_from(Statistic)
                .where(and_(Statistic.date >= date_from, Statistic.date <= date_to))
            )
            result = await session.execute(query)
            return [result.all()]

    async def delete_all_statistics(self) -> None:
        async with self.session() as session:
            query = (
                delete(Statistic)
            )
            await session.execute(query)
            await session.commit()


# if __name__ == '__main__':
#     session = asyncio.run(make_session())
#     dao = StatisticDAO(session)
#     # asyncio.run(dao.create_statistic(date(2024, 1, 31), 50, 1, 12))
#     # print(asyncio.run(dao.get_statistics(date(2022, 4, 13), date(2024, 1, 31))))
#     asyncio.run(dao.delete_all_statistics())
