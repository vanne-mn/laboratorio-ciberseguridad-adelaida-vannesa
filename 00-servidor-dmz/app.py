
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


class CustomHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )
        self.end_headers()

        # Personalización del laboratorio
        estudiante = os.getenv(
            "ESTUDIANTE_NOMBRE",
            "Adelaida y Vannesa"
        )

        html_content = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Servidor Web DMZ - Adelaida y Vannesa</title>

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f4f4f9;
                }}

                .container {{
                    background: white;
                    padding: 25px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    max-width: 800px;
                    margin: auto;
                }}

                h1 {{
                    color: #2c3e50;
                }}

                h2 {{
                    color: #34495e;
                }}

                .status {{
                    color: #27ae60;
                    font-weight: bold;
                }}

                .integrantes {{
                    color: #2980b9;
                    font-weight: bold;
                }}

                hr {{
                    border: 0;
                    border-top: 1px solid #ddd;
                    margin: 20px 0;
                }}
            </style>
        </head>

        <body>
            <div class="container">

                <h1>🛡️ Servidor Objetivo DMZ</h1>

                <h2>Servidor DMZ Activo</h2>

                <p>
                    Estado del servicio:
                    <span class="status">ONLINE / ACTIVO</span>
                </p>

                <hr>

                <p>
                    <strong>Laboratorio de Ciberseguridad:</strong>
                    <span class="integrantes">{estudiante}</span>
                </p>

                <p>
                    Este nodo actúa como objetivo central para
                    las pruebas controladas de tráfico y análisis de logs.
                </p>

                <hr>

                <p>
                    <strong>Integrantes:</strong>
                    Adelaida y Vannesa
                </p>

                <p>Laboratorio académico de ciberseguridad.</p>

            </div>
        </body>
        </html>
        """

        self.wfile.write(html_content.encode("utf-8"))


if __name__ == "__main__":

    # Render proporciona el puerto mediante la variable PORT.
    # En ejecución local utilizamos el puerto 8080.
    port = int(os.environ.get("PORT", 8080))

    server_address = ("0.0.0.0", port)

    httpd = HTTPServer(server_address, CustomHandler)

    print(f"Servidor DMZ iniciado en el puerto {port}...")
    print("Integrantes: Adelaida y Vannesa")
    print("Estado: ONLINE / ACTIVO")

    httpd.serve_forever()
