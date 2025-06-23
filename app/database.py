import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

print(f"Connecting to DB at host={POSTGRES_HOST}, db={POSTGRES_DB}")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Функция для подключения к базе данных
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

# Создание таблицы
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            position VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()