# Базовий образ з Python
FROM python:3.10-slim

# Робоча директорія в контейнері
WORKDIR /app

# Копіюємо файли залежностей
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту файлів проєкту
COPY . .

# Команда за замовчуванням: запуск головного файлу
CMD ["python", "app/main.py"]