
#!/bin/sh

TARGET="https://servidor-dmz-adelaida-vannesa.onrender.com"

echo "=========================================="
echo "MODULO 01 - SIMULACION DE TRAFICO HTTP"
echo "Laboratorio: Adelaida y Vannesa"
echo "=========================================="

for i in $(seq 1 5); do
    echo "Solicitud de prueba $i"

    curl --max-time 10 -s -o /dev/null \
        -w "Codigo HTTP: %{http_code}\n" \
        "$TARGET"

    sleep 2
done

echo "=========================================="
echo "SIMULACION FINALIZADA"
echo "Se realizaron 5 solicitudes controladas."
echo "=========================================="
