from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

estudiantes = [
    {
        "id": 1,
        "nombre": "Alex",
        "apellido": "Tola",
        "carrera": "Economia",
    },
    {
        "id": 2,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 3,
        "nombre": "Lucas",
        "apellido": "Calderon",
        "carrera": "Desarrollador de software",
    },
    {
        "id": 4,
        "nombre": "Alex",
        "apellido": "Mamani",
        "carrera": "Economia",
    },
]




class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):    
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def do_GET(self):
        if self.path == "/estudiantes":
            self.response_handler(200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                self.response_handler(200, estudiante)
        elif self.path == "/carreras":
            carrera = list({estudiante["carrera"] for estudiante in estudiantes})
            self.response_handler(200, carrera)

        elif self.path == "/Economia":
            estudiantes_economia = [estudiante for estudiante in estudiantes if estudiante["carrera"] == "Economia"]
            self.response_handler(200, estudiantes_economia)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_POST(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.response_handler(201, estudiantes)

        else:
            self.response_handler(201, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/estudiantes"):
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            id = data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(data)
                self.response_handler(201, estudiante)

        else:
            self.response_handler(201, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path == "/estudiantes":
            estudiantes.clear()
            self.response_handler(201, estudiantes)
        else:
            self.response_handler(201, {"Error": "Ruta no existente"})

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()