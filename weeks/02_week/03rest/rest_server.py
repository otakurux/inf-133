from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Juanito",
        "apellido": "Perez",
        "carrera": "Medicina",
    },
    {
        "id": 3,
        "nombre": "Maria",
        "apellido": "Lopez",
        "carrera": "Derecho",
    },
    {
        "id": 4,
        "nombre": "Ana",
        "apellido": "Martinez",
        "carrera": "Administración de Empresas",
    },
    {
        "id": 5,
        "nombre": "Luis",
        "apellido": "Gonzalez",
        "carrera": "Arquitectura",
    },
    {
        "id": 6,
        "nombre": "pablo",
        "apellido": "Tola",
        "carrera": "Derecho",
    }
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/eliminar_estudiante":
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path.startswith("/buscar_estudiante_id/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        
        
        elif self.path.startswith("/buscar_nombre/"):
            initial = self.path.split("/")[-1]
            buscar_nombre = [estudiante["nombre"] for estudiante in estudiantes if estudiante["nombre"].lower().startswith(initial.lower())]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(buscar_nombre).encode("utf-8"))
            
        elif self.path == "/contar_carreras":
            count_per_mayor = {}
            for student in estudiantes:
                carrera = student["carrera"]
                count_per_mayor[carrera] = count_per_mayor.get(carrera, 0) + 1
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(count_per_mayor).encode("utf-8"))

            
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/actualizar_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            id = post_data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(post_data)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))


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