from app.services.statistic_service import StatisticService
from app.dao.statistic_dao import StatisticDAO
from app.db import make_session
from app.schemas.statistic_schema import StatisticSchema
from fastapi import APIRouter, HTTPException, status
from datetime import date

router = APIRouter()

@router.get('/statistics/{from}/{to}', status_code=status.HTTP_200_OK)
async def get_statistics(date_from: date, date_to: date):
    session = await make_session()
    dao = StatisticDAO(session)
    service = StatisticService(dao)
    try:
        result = await service.get_statistics(date_from, date_to)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post('/add_statistic/{date}', status_code=status.HTTP_201_CREATED)
async def add_statistic(statistic: StatisticSchema) -> None:
    session = await make_session()
    dao = StatisticDAO(session)
    service = StatisticService(dao)
    await service.add_statistic(statistic.date, statistic.views, statistic.clicks, statistic.cost)

@router.delete('/delete_all_statistics', status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_statistics() -> None:
    session = await make_session()
    dao = StatisticDAO(session)
    service = StatisticService(dao)
    await service.delete_all_statistic()
