from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field


class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()


class CrearEstudiante(ObjectType):
    estudiante = Field(Estudiante)

    class Arguments:
        nombre = String()
        apellido = String()
        carrera = String()

    def mutate(root, info, nombre, apellido, carrera):
        nuevo_estudiante = Estudiante(
            id=len(estudiantes) + 1,
            nombre=nombre,
            apellido=apellido,
            carrera=carrera
        )
        estudiantes.append(nuevo_estudiante)
        return CrearEstudiante(estudiante=nuevo_estudiante)


class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id = Field(Estudiante, id=Int())
    estudiante_por_nombre_apellido = Field(Estudiante, nombre=String(), apellido=String())
    estudiantes_arquitectura = List(Estudiante)

    def resolve_estudiantes(root, info):
        return estudiantes

    def resolve_estudiante_por_id(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None

    def resolve_estudiante_por_nombre_apellido(root, info, nombre, apellido):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre and estudiante.apellido == apellido:
                return estudiante
        return None

    def resolve_estudiantes_arquitectura(root, info):
        estudiantes_arquitectura = []
        for estudiante in estudiantes:
            if estudiante.carrera == "Arquitectura":
                estudiantes_arquitectura.append(estudiante)
        return estudiantes_arquitectura


estudiantes = [
    Estudiante(
        id=1,
        nombre="Pedrito",
        apellido="García",
        carrera="Ingeniería de Sistemas"
    ),
    Estudiante(
        id=2,
        nombre="Jose",
        apellido="Lopez",
        carrera="Arquitectura"
    ),
]

schema = Schema(query=Query, mutation=CrearEstudiante)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
