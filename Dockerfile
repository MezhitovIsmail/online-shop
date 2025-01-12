# Используем официальный Python-образ  
FROM python:3.9-slim

# Устанавливаем необходимые зависимости
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    python3-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из папки app в контейнер
COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

# Экспонируем порт для Flask-приложения
EXPOSE 5000

# Указываем команду для запуска приложения
CMD ["python", "app.py"]
