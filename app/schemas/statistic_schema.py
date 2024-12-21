from pydantic import BaseModel
from datetime import date

class StatisticSchema(BaseModel):
    date: date
    views: int
    clicks: int
    cost: float
