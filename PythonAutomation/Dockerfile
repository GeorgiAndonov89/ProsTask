# 1. Използваме официалния образ на Python
FROM python:3.9-slim

# 2. Задаваме работната директория в контейнера
WORKDIR /app

# 3. Копираме изискванията на Python (ако имаме requirements.txt)
COPY requirements.txt .

# 4. Инсталираме зависимостите от requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копираме целия проект в контейнера
COPY . /app

# 6. Задаваме командата за стартиране на FastAPI приложението
CMD ["uvicorn", "Task.TaskPros:app", "--host", "0.0.0.0", "--port", "8000"]

# 7. Отваряме порт 8000
EXPOSE 8000
