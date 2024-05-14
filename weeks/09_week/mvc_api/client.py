import requests

BASE_URL = "http://localhost:5000/api"
headers = {"Content-Type": "application/json"}

def create_animal(name, species, age):
    url = f"{BASE_URL}/animals"
    animal_data = {"name": name, "species": species, "age": age}
    response = requests.post(url, json=animal_data, headers=headers)
    return response.json()

def get_animals():
    url = f"{BASE_URL}/animals"
    response = requests.get(url, headers=headers)
    return response.json()

def get_animal_details(animal_id):
    url = f"{BASE_URL}/animals/{animal_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def update_animal(animal_id, name=None, species=None, age=None):
    url = f"{BASE_URL}/animals/{animal_id}"
    animal_data = {}
    if name is not None:
        animal_data["name"] = name
    if species is not None:
        animal_data["species"] = species
    if age is not None:
        animal_data["age"] = age
    response = requests.put(url, json=animal_data, headers=headers)
    return response.json()

def delete_animal(animal_id):
    url = f"{BASE_URL}/animals/{animal_id}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        return f"Animal con ID {animal_id} eliminado con éxito."
    else:
        return f"Error: {response.status_code} - {response.text}"

def list_animals():
    return [
        {
            "name": "Lion",
            "especie": "Panthera leo",
            "age": "10"
        },
        {
            "name": "Tiger",
            "especie": "Panthera tigris",
            "age": "8"
        },
        {
            "name": "Elephant",
            "especie": "Loxodonta africana",
            "age": "20"
        },
        {
            "name": "Giraffe",
            "especie": "Giraffa camelopardalis",
            "age": "5"
        },
        {
            "name": "Zebra",
            "especie": "Equus quagga",
            "age": "3"
        },
        {
            "name": "Cheetah",
            "especie": "Acinonyx jubatus",
            "age": "6"
        },
        {
            "name": "Hippopotamus",
            "especie": "Hippopotamus amphibius",
            "age": "15"
        },
        {
            "name": "Kangaroo",
            "especie": "Macropus",
            "age": "4"
        },
        {
            "name": "Penguin",
            "especie": "Spheniscidae",
            "age": "2"
        },
        {
            "name": "Gorilla",
            "especie": "Gorilla",
            "age": "12"
        }
    ]

if __name__ == "__main__":
    print("Creando nuevos animales:")
    animals = list_animals()
    nuevo_animal = [create_animal(animal["name"], animal["especie"], animal["age"]) for animal in animals]
    print(nuevo_animal)

    print("\nObteniendo la lista de animales:")
    lista_animales = get_animals()
    print(lista_animales)

    print("\nObteniendo detalles del animal con ID 1:")
    animal_detallado = get_animal_details(1)
    print(animal_detallado)

    print("\nActualizando el animal con ID 1:")
    datos_actualizacion = {"name": "Tigre", "species": "Felino", "age": 4}
    animal_actualizado = update_animal(1, **datos_actualizacion)
    print(animal_actualizado)

    print("\nEliminando el animal con ID 1:")
    mensaje_eliminar = delete_animal(1)
    print(mensaje_eliminar)
