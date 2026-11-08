
FROM alpine:3

# Instalar herramientas para consultas DNS
RUN apk add --no-cache bind-tools

WORKDIR /app

# Copiar el script de simulación
COPY entrypoint.sh /app/entrypoint.sh

# Dar permisos de ejecución
RUN chmod +x /app/entrypoint.sh

# Ejecutar la simulación al iniciar el contenedor
CMD ["/app/entrypoint.sh"]
