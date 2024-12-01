# Образ
FROM python:3.11-slim

# Переменная окружения для управления буферизацией вывода
ENV PYTHONUNBUFFERED=1

# Рабочая директория внутри контейнера
WORKDIR /HW1

# Файлы проекта
COPY . /HW1

# Зависимости системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установить Poetry.
RUN pip install --no-cache-dir poetry

# Скопируйте только файлы зависимостей для более эффективного кеширования слоя
COPY pyproject.toml poetry.lock /HW1/

# Установите зависимости проекта
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev

# Команда для запуска сценария анализа логов
CMD ["python", "parser.py"]