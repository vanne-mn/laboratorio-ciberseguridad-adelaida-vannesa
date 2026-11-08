
FROM alpine:3

WORKDIR /app

# Crear un archivo ficticio para simular una dependencia no autorizada
# Su contenido es inofensivo y nunca se ejecutará
RUN echo "ARCHIVO DE PRUEBA - DEPENDENCIA NO AUTORIZADA SIMULADA" \
    > /app/malicious_dependency.sh

# Copiar el script de verificación
COPY entrypoint.sh /app/entrypoint.sh

# Dar permisos de ejecución al verificador
RUN chmod +x /app/entrypoint.sh

# Ejecutar el script utilizando explícitamente el intérprete sh
CMD ["sh", "/app/entrypoint.sh"]
