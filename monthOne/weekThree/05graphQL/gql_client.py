import requests

query = """
    {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query': query})
print(response.text)

