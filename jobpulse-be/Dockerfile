FROM python:3.11-slim
WORKDIR /app
# Make sure you have a requirements.txt with fastapi, uvicorn, and elasticsearch
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]