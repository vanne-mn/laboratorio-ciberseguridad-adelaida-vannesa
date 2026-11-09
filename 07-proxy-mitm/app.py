
from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    print("\n==========================================", flush=True)
    print("MODULO 07 - SIMULACION PROXY MITM", flush=True)
    print("Laboratorio: Adelaida y Vannesa", flush=True)
    print("==========================================", flush=True)

    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Modulo 07 - Proxy MITM</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f1f4f8;
                margin: 40px;
                color: #263238;
            }
            .contenedor {
                max-width: 750px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 3px 12px #0002;
            }
            h1 { color: #253b65; }
            .estado { color: #16834a; font-weight: bold; }
            .alerta {
                background: #fff3cd;
                padding: 15px;
                border-radius: 8px;
                color: #795600;
            }
        </style>
    </head>
    <body>
        <div class="contenedor">
            <h1>Modulo 07 - Proxy MITM</h1>
            <h2>Simulacion educativa</h2>

            <p>Laboratorio de Ciberseguridad</p>
            <p><strong>Integrantes:</strong> Adelaida y Vannesa</p>

            <p>Estado del servicio:
                <span class="estado">ONLINE / ACTIVO</span>
            </p>

            <div class="alerta">
                <strong>Demostracion controlada:</strong>
                Este modulo representa el funcionamiento conceptual
                de un intermediario que puede observar y modificar
                una comunicacion.
            </div>

            <p>No se intercepta trafico real ni se capturan credenciales.</p>

            <p>
                <a href="/simulacion">Ejecutar simulacion MITM</a>
            </p>
        </div>
    </body>
    </html>
    """

@app.route("/simulacion", methods=["GET"])
def simulacion():
    print("[MITM] Solicitud ficticia recibida.", flush=True)
    print("[MITM] Se analiza una comunicacion de demostracion.", flush=True)
    print("[MITM] Se simula una alteracion de respuesta.", flush=True)
    print("[MITM ALERTA] Posible modificacion de informacion en transito.", flush=True)
    print("[MITM] No se intercepto trafico real.", flush=True)

    return jsonify({
        "modulo": "07 - Proxy MITM",
        "laboratorio": "Adelaida y Vannesa",
        "tipo": "Simulacion educativa",
        "solicitud": "Ficticia",
        "intermediario": "Simulado",
        "alteracion": "Demostracion conceptual",
        "alerta": "Posible modificacion de informacion en transito",
        "trafico_real_interceptado": False,
        "credenciales_capturadas": False,
        "fecha": datetime.now().isoformat()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
