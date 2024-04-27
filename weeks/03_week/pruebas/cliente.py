import requests
url = 'http://localhost:8000/graphql'


query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""

response = requests.post(url, json={'query': query_lista})
print(response.text)

query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""


response = requests.post(url, json={'query': query})
print(response.text)


query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

response = requests.post(url, json={'query': query_lista})
print(response.text)

query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

response = requests.post(url, json={'query': query_lista})
print(response.text)