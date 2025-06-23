from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import create_table
from app.routers import users, auth

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

create_table()

app.include_router(users.router)
app.include_router(auth.router)