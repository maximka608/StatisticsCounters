from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import date

BaseModel = declarative_base()

class Statistic(BaseModel):
    __tablename__ = 'statistic'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date]
    views: Mapped[int] = mapped_column(default=0)
    clicks: Mapped[int] = mapped_column(default=0)
    cost: Mapped[float] = mapped_column(default=0.0)
