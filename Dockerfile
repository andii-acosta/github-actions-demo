# Imagen base oficial con Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY . .

# Comando por defecto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
