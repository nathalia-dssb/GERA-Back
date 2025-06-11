from fastapi import FastAPI
from app.db.database import init_db
from app.api import routes 

app = FastAPI(
    title="FastAPI SQLite App",
    version="1.0.0"
)

init_db()

app.include_router(routes.router)
