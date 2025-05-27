# Используем официальный образ Python
FROM python:3.10-slim

# Рабочая директория в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY . .

# Expose порт приложения (по умолчанию Flask обычно 5000)
EXPOSE 5000

# CMD убираем, чтобы запускать команду из docker-compose
Пример docker-compose.yml (с CMD)
yaml
Копировать
Редактировать
version: '3.8'

services:
  flaskapp:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - FLASK_APP=app.py  # или твой главный файл
    command: flask run --host=0.0.0.0 --port=5000
    volumes:
      - .:/app  # Для разработки, чтобы изменения сразу отражались в контейнере