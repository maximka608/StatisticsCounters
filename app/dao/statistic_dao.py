from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import and_, select, delete
from app.models.statistic import Statistic
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

    async def get_statistics(self, date_from: date, date_to: date):
        async with self.session() as session:
            query = (
                select(Statistic).select_from(Statistic)
                .order_by(Statistic.date)
                .where(and_(Statistic.date >= date_from, Statistic.date <= date_to))
            )
            result = await session.execute(query)
            return result

    async def delete_all_statistics(self) -> None:
        async with self.session() as session:
            query = (
                delete(Statistic)
            )
            await session.execute(query)
            await session.commit()
