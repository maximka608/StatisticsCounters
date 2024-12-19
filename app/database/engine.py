from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
import os

load_dotenv()

def create_url():
    driver_db = os.getenv("DRIVER_DB")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    name_db = os.getenv("NAME_DB")

    url = f"postgresql+{driver_db}://{username}:{password}@{host}:{port}/{name_db}"
    return url


async def make_engine() -> AsyncEngine:
    url = create_url()
    engine = create_async_engine(url)
    return engine
