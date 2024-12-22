from datetime import date
from app.dao.statistic_dao import StatisticDAO
from app.schemas.statistic_schema import StatisticDTO

class StatisticService:
    def __init__(self, statistic_dao: StatisticDAO) -> None:
        self.dao = statistic_dao

    async def get_statistics(self, date_from: date, date_to: date):
        if date_from > date_to:
            raise ValueError(f"Invalid date range: 'From' ({date_from}) cannot be greater than 'To' ({date_to}).")
        result, response = await self.dao.get_statistics(date_from, date_to), []
        for row in result.scalars():
            stat_dto = StatisticDTO.model_validate(row.__dict__, from_attributes=True)
            stat_dto.avg_cost_clicks = row.cost / row.clicks if row.clicks > 0 else 0
            stat_dto.avg_cost_1000_views = row.cost / row.views * 1000 if row.views > 0 else 0
            response.append(stat_dto)
        return response

    async def add_statistic(self, date: date, views: int, clicks: int, cost: float) -> None:
        await self.dao.add_statistic(date, views, clicks, cost)

    async def delete_all_statistic(self) -> None:
        await self.dao.delete_all_statistics()
