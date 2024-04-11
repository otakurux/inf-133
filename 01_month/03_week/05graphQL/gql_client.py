# import requests

# query = """
#     {
#         crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia"){
#             estudiante{
#                 id
#                 nombre
#                 apellido
#                 carrera
#             }
#         }
#     }
# """

# url = 'http://localhost:8000/graphql'

# response = requests.post(url, json={'query': query})
# print(response.text)

import requests
import json

url = "http://localhost:8000/graphql"

def devolve_estudiantes():
    query_all_students = """
    {
    estudiantes {
        id
        nombre
        apellido
        carrera
    }
    }
    """

    response = requests.post(url, json={"query": query_all_students})

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))
    else:
        print("Error:", response.status_code)



def crear_estudiante(nombre, apellido, carrera, url):

    mutation_create_student = """
    mutation {
      crearEstudiante(nombre: "%s", apellido: "%s", carrera: "%s") {
        estudiante {
          id
          nombre
          apellido
          carrera
        }
      }
    }
    """ % (nombre, apellido, carrera)

    response = requests.post(url, json={"query": mutation_create_student})

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": response.status_code}

nombre = "Juan"
apellido = "Perez"
carrera = "Ingenieria Informatica"

# result = crear_estudiante(nombre, apellido, carrera, url)
# print(json.dumps(result, indent=2))

devolve_estudiantes()