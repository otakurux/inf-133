import requests

url = 'http://localhost:5000/'

response = requests.get(url)

if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

params = {'nombre': 'un_nombre'}
response = requests.get(url+'saludar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

params = {'num1': 5, 'num2': 3}
response = requests.get(url+'sumar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

params = {'cadena': 'reconocer'}
response = requests.get(url+'palindromo', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

params = {'cadena': 'exepciones', 'vocal': 'e'}
response = requests.get(url+'contar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
