
#!/bin/sh

TARGET="https://servidor-dmz-adelaida-vannesa.onrender.com"

# Rutas públicas de demostración
RUTAS="/ /index.html /ruta-publica-demo"

echo "=========================================="
echo "MODULO 03 - SIMULACION DE RECONOCIMIENTO"
echo "Laboratorio: Adelaida y Vannesa"
echo "=========================================="

echo "Servidor objetivo autorizado: $TARGET"
echo ""

for ruta in $RUTAS; do
    echo "Consultando ruta: $ruta"

    CODE=$(curl --max-time 10 -s -o /dev/null \
        -w "%{http_code}" "$TARGET$ruta")

    echo "Codigo de respuesta HTTP: $CODE"
    echo ""

    sleep 2
done

echo "=========================================="
echo "SIMULACION FINALIZADA"
echo "Se consultaron 3 rutas de demostracion."
echo "No se accedio a archivos privados."
echo "=========================================="
