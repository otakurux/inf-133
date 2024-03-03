import requests
import json


url = "http://localhost:8000/"


print()
def get_carrera():
    route_carrera = url + "carreras"
    response = requests.get(route_carrera)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

print(get_carrera())


print()
def add_estudiante(nombre, apellido, carrera):
    route_Economia = url + "estudiantes"
    nuevo_estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    }
        
    response = requests.post(route_Economia, json=nuevo_estudiante)
    if response.status_code == 201:
        return "Estudiante agregado exitosamente."
    else:
        return "Error:", response.text
    
print(add_estudiante("Juan", "Lopez", "Economia"))
print(add_estudiante("Paolo", "Arias", "Economia"))


print()
def get_estudiantes_economia():
    route_Economia = url + "estudiantes"    
    response = requests.get(route_Economia)
    if response.status_code == 200:
        estudiantes_economia = response.json()
        print("Estudiantes de Economia:")
        for estudiante in estudiantes_economia:
            print(f"- {estudiante['nombre']} {estudiante['apellido']}")
    else:
        print("Error:", response.text)
        
get_estudiantes_economia()