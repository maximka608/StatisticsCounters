from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import date

BaseModel = declarative_base()

class Statistic(BaseModel):
    __tablename__ = 'statistic'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date]
    views: Mapped[int]
    clicks: Mapped[int]
    cost: Mapped[float]
