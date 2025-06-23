from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.database import get_db_connection

router = APIRouter()

@router.get("/users/", response_model=List[User])
async def read_all_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, email, password, name, position FROM users")
    users = [User(id=row[0], email=row[1], password=row[2], name=row[3], position=row[4]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return users

@router.post("/users/", response_model=User)
async def create_user(user: User):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (email, password, name, position) VALUES (%s, %s, %s, %s) RETURNING id", (user.email, user.password, user.name, user.position))
        user_id = cur.fetchone()[0]
        conn.commit()
        return User(id=user_id, email=user.email, password=user.password, name=user.name, position=user.position)
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, email, password, name, position FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")

        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return User(id=user[0], email=user[1], password=user[2], name=user[3], position=user[4])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()