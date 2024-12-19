from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.models.statistic import Statistic
from typing import Any, List
from datetime import date

class StatisticDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_statistic(self, date: date, views: int, clicks: int, cost: float) -> None:
        async with self.session:
            statistic_obj = Statistic(date=date, views=views, clicks=clicks, cost=cost)
            self.session.add(statistic_obj)
            await self.session.commit()

    async def get_statistics(self, date_from: date, date_to: date) -> List[Any]:
        query = (
            select(Statistic.date).select_from(Statistic)
        )
        result = await self.session.execute(query)
        return [result.all()]

    async def delete_all_statistics(self) -> None:
        query = (
            delete(Statistic)
        )
        await self.session.execute(query)
