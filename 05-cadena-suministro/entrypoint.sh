
#!/bin/sh

echo "=========================================="
echo "MODULO 05 - SEGURIDAD EN LA CADENA DE SUMINISTRO"
echo "Laboratorio: Adelaida y Vannesa"
echo "=========================================="

echo ""
echo "Verificando integridad del contenedor..."
echo ""

if [ -f "/app/malicious_dependency.sh" ]; then

    echo "[ALERTA DE SEGURIDAD]"
    echo "Se detecto una dependencia no autorizada."
    echo "Archivo: /app/malicious_dependency.sh"
    echo "Accion: archivo identificado, pero NO ejecutado."

else

    echo "[OK] No se detectaron archivos sospechosos."

fi

echo ""
echo "=========================================="
echo "VERIFICACION FINALIZADA"
echo "No se ejecuto codigo malicioso."
echo "=========================================="
