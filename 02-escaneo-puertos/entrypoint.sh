
#!/bin/sh

HOST="servidor-dmz-adelaida-vannesa.onrender.com"

echo "=========================================="
echo "MODULO 02 - RECONOCIMIENTO DE PUERTOS"
echo "Laboratorio: Adelaida y Vannesa"
echo "=========================================="

echo "Objetivo autorizado: nuestro servidor DMZ"
echo "Host: $HOST"
echo ""

echo "Comprobando conectividad HTTPS..."

if curl --max-time 10 -s -o /dev/null \
    -w "Puerto HTTPS 443 - Codigo HTTP: %{http_code}\n" \
    "https://$HOST"; then
    echo "Comprobacion HTTPS finalizada."
else
    echo "No fue posible completar la solicitud HTTPS."
fi

echo ""
echo "=========================================="
echo "RECONOCIMIENTO FINALIZADO"
echo "No se realizaron escaneos masivos."
echo "=========================================="
