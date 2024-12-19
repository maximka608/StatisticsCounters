from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()

Statistics = [
    {'date': datetime.strptime('2024-01-31', "%Y-%m-%d").date(), 'views': 50, 'clicks': 1, 'cost': 12},
    {'date': datetime.strptime('2022-04-13', "%Y-%m-%d").date(), 'views': 100, 'clicks': 5, 'cost': 20}
]

@app.get('/statistics/{from}/{to}')
def get_statistics(date_from: datetime, date_to: datetime):
    results = []
    for stat in Statistics:
        if stat['date'] > date_from.date() and stat['date'] < date_to.date():
            results.append(stat)
    return results

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
