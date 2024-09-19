FROM python:3.12-slim

# Define a variável de ambiente para não gerar arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Desabilita o buffer de stdout/stderr
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
