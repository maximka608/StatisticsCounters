from pydantic import BaseModel
from typing import Optional
from datetime import date

class StatisticSchema(BaseModel):
    date: date
    views: int
    clicks: int
    cost: float


class StatisticDTO(StatisticSchema):
    avg_cost_clicks: Optional[float] = None
    avg_cost_1000_views: Optional[float] = None
