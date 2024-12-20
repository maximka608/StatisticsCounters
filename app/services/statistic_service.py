from datetime import date

class StatisticService:
    def __init__(self, statistic_dao) -> None:
        self.dao = statistic_dao

    def get_statistics(self, date_from: date, date_to: date):
        pass

    def add_statistic(self, date: date, views: int, clicks: int, cost: float) -> None:
        pass

    def delete_all_statistic(self) -> None:
        pass
