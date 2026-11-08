
FROM alpine:3

# Instalar únicamente curl para comprobar la conexión HTTPS
RUN apk add --no-cache curl

WORKDIR /app

# Copiar el script de reconocimiento
COPY entrypoint.sh /app/entrypoint.sh

# Dar permisos de ejecución
RUN chmod +x /app/entrypoint.sh

# Ejecutar la comprobación al iniciar el contenedor
CMD ["/app/entrypoint.sh"]
