from datetime import date
from app.dao.statistic_dao import StatisticDAO

class StatisticService:
    def __init__(self, statistic_dao: StatisticDAO) -> None:
        self.dao = statistic_dao

    async def get_statistics(self, date_from: date, date_to: date):
        if date_from > date_to:
            raise ValueError(f"Invalid date range: 'From' ({date_from}) cannot be greater than 'To' ({date_to}).")
        result = await self.dao.get_statistics(date_from, date_to)
        for res in result:
            print(res)
        return result

    async def add_statistic(self, date: date, views: int, clicks: int, cost: float) -> None:
        await self.dao.add_statistic(date, views, clicks, cost)

    async def delete_all_statistic(self) -> None:
        await self.dao.delete_all_statistics()
