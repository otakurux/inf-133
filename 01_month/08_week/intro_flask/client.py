import requests

base_url = "http://127.0.0.1:5000"

def response_server(response):
    if response.status_code == 200:
        print("Respuesta del servidor:")
        print(response.text)
    else:
        print("Error al conectar con el servidor:", response.status_code)

def probar_hello_world():
    response = requests.get(base_url + "/")
    response_server(response)

def probar_saludar(nombre):
    response = requests.get(base_url + "/saludar", params={"nombre": nombre})
    response_server(response)

def probar_sumar(num1, num2):
    response = requests.get(base_url + "/sumar", params={"num1": num1, "num2": num2})
    response_server(response)

def probar_palindromo(cadena):
    response = requests.get(base_url + "/palindromo", params={"cadena": cadena})
    response_server(response)

def probar_contar(cadena, vocal):
    response = requests.get(base_url + "/contar", params={"cadena": cadena, "vocal": vocal})
    response_server(response)

if __name__ == "__main__":
    probar_hello_world()
    probar_saludar("un nombre")
    probar_sumar(5, 3)
    probar_palindromo("reconocer")
    probar_contar("exepciones", "e")
