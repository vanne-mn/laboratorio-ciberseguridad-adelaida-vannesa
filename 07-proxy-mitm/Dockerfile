
FROM python:3-alpine

# Mostrar los mensajes inmediatamente en la consola
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar la aplicación
COPY app.py /app/app.py

# Instalar Flask
RUN pip install --no-cache-dir flask

# Puerto de la aplicación
ENV PORT=8080
EXPOSE 8080

# Iniciar el servidor
CMD ["python", "app.py"]
