
FROM alpine:3

# Instalar curl para las solicitudes HTTP controladas
RUN apk add --no-cache curl

WORKDIR /app

# Copiar el script de simulación
COPY entrypoint.sh /app/entrypoint.sh

# Dar permisos de ejecución
RUN chmod +x /app/entrypoint.sh

# Ejecutar la simulación al iniciar el contenedor
CMD ["/app/entrypoint.sh"]
