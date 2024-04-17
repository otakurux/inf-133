import requests

def response_server(response):
    if response.status_code == 200:
        print("Respuesta del servidor:")
        print(response.text)
    else:
        print("Error al conectar con el servidor:", response.status_code)
    

url = 'http://localhost:5000/'
response = requests.get(url)
response_server(response)

params = {'nombre': 'un_nombre'}
response = requests.get(url+'saludar', params=params)
response_server(response)

params = {'num1': 5, 'num2': 3}
response = requests.get(url+'sumar', params=params)
response_server(response)

params = {'cadena': 'reconocer'}
response = requests.get(url+'palindromo', params=params)
response_server(response)

params = {'cadena': 'exepciones', 'vocal': 'e'}
response = requests.get(url+'contar', params=params)
response_server(response)
