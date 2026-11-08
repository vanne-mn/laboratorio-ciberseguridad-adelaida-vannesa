
#!/bin/sh

# Dominio de nuestro servidor DMZ
DOMINIO="servidor-dmz-adelaida-vannesa.onrender.com"

# Etiqueta ficticia: no contiene datos personales ni credenciales
ETIQUETA="simulacion-dns-laboratorio"

echo "=========================================="
echo "MODULO 04 - SIMULACION DE CONSULTA DNS"
echo "Laboratorio: Adelaida y Vannesa"
echo "=========================================="

echo "Dominio de prueba: $DOMINIO"
echo "Etiqueta de demostracion: $ETIQUETA"
echo ""

echo "Realizando consulta DNS controlada..."

nslookup "${ETIQUETA}.${DOMINIO}"

echo ""
echo "=========================================="
echo "SIMULACION FINALIZADA"
echo "Se utilizo una etiqueta ficticia."
echo "No se transmitieron datos confidenciales."
echo "=========================================="
