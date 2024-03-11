import requests

query = """
    {
        resolve_estudiante_arquitectura
    }
"""

url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query': query})
print(response.text)


        # estudiantePorNameSurname(name: "Jose" surname: "Lopez"){
        #     nombre
        # }