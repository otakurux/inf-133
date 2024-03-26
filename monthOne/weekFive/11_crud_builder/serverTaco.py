from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Taco:
    def __init__(self):
        self.tortilla = none
        self.tuco = none

    def _str__(self):
        return f"Tortilla: {tortilla}, Tuco: {tuco}"

class CreateTaco:
    def __init__(self):
        self.taco = Taco()

    def set_tortilla(tortilla):
        self.taco.tortilla = tortilla

    def set_tuco(tuco):
        self.taco.tuco = tuco

Tacos = {}

class PizzaHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):    
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def read_taco(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        if self.path == "/taco":
            self.response_handler(200, estudiantes)
            
        elif self.path.startswith("/taco/"):
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

    def cr¡tf):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            
            self.response_handler(201, estudiantes)

        else:
            self.response_handler(201, {"Error": "Ruta no existente"})