
FROM python:3-alpine

WORKDIR /app

# Copiar el servidor DMZ
COPY app.py /app/app.py

# Puerto predeterminado para ejecución local
ENV PORT=8080

EXPOSE 8080

# Iniciar el servidor
CMD ["python", "app.py"]
