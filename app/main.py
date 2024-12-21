from fastapi import FastAPI
from app.controllers.statistic_controller import router as statistic_router
import uvicorn

app = FastAPI()

app.include_router(statistic_router, tags=['Statistic'])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
