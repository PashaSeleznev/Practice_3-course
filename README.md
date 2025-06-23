# Проект: FastAPI + PostgreSQL + Docker

## Описание

Этот проект создан для знакомства с Docker и его применением при работе с FastAPI.  
В проекте реализован простой личный кабинет пользователя для автоматического склада инструментов.

Основные технологии:  
- FastAPI — backend  
- PostgreSQL (image postgres:15) — база данных  
- Docker и Docker Compose — контейнеризация и оркестрация  
- Чистые HTML и CSS — frontend

---

## Структура проекта

docker-compose.yml
dockerfile
requirements.txt
/app
├── database.py
├── main.py
├── /models
│ └── user.py
├── /routers
│ ├── auth.py
│ └── users.py
├── /static
│ ├── styles.css
│ └── /images
└── /templates
  ├── login.html
  ├── profile.html
  └── register.html

---

## Функционал

- Регистрация нового пользователя  
- Удаление существующего пользователя  
- Личный кабинет пользователя  

---

## Запуск проекта

1. Убедитесь, что Docker и Docker Compose установлены:  
   https://docs.docker.com/get-docker/

2. Запустите контейнеры с помощью команды:

```bash
docker compose up --build -d
```

3. При первом запуске создаётся база данных на основе образа postgres:15.
Если подключение к БД не произошло сразу, попробуйте перезапустить контейнеры:

```bash
docker compose down && docker compose up -d
```

4. Для просмотра логов веб-приложения используйте:
```bash
docker compose logs -f web
```

Для отображения страниц в браузере, нужно посмотреть свой IP:

```bash
ip a
```
И перейти в нем на порт 8000/.
