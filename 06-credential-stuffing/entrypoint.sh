
#!/bin/sh

# Usuarios ficticios para la simulacion
USUARIOS="admin root user docente gestor"

echo "=========================================="
echo "MODULO 06 - SIMULACION CREDENTIAL STUFFING"
echo "Laboratorio: Adelaida y Vannesa"
echo "=========================================="

echo ""
echo "Analizando intentos de autenticacion ficticios..."
echo ""

TOTAL=0

for usuario in $USUARIOS; do
    TOTAL=$((TOTAL + 1))

    echo "Intento simulado $TOTAL"
    echo "Usuario de prueba: $usuario"
    echo "Estado: INTENTO FICTICIO REGISTRADO"
    echo ""
done

echo "=========================================="
echo "ANALISIS DE SEGURIDAD"
echo "=========================================="

echo "Total de intentos simulados: $TOTAL"
echo "Patron detectado: multiples usuarios."
echo "Alerta: posible comportamiento de Credential Stuffing."
echo "No se enviaron credenciales ni solicitudes de acceso."

echo ""
echo "SIMULACION FINALIZADA"
echo "=========================================="
