FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Puerto donde la aplicación web escucha
EXPOSE 8080

# Comando por defecto para iniciar la aplicación
CMD ["python", "app.py"]