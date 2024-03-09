import requests

query = """
    {
        estudiante(id: 1, nombre: "Jose"){
            nombre
        }
    }
"""

url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query': query})
print(response.text)