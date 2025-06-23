from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models.user import User, UserLogin
from app.database import get_db_connection
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register/", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/profile/{user_id}", response_class=HTMLResponse)
async def profile(request: Request, user_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, email, password, name, position FROM users WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = User(id=user_data[0], email=user_data[1], password=user_data[2], name=user_data[3], position=user_data[4])
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})

@router.post("/login/")
async def login(user: UserLogin):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, email, password, name, position FROM users WHERE email = %s AND password = %s", (user.email, user.password))
        user_data = cur.fetchone()
        if user_data is None:
            raise HTTPException(status_code=401, detail="Неверный адрес электронной почты или пароль")
        user_id = user_data[0]
        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
