import requests
import json

# Configuración de la URL base del servidor
BASE_URL = 'http://localhost:8000'

# Función para enviar una solicitud GET y mostrar la respuesta
def get_chocolates():
    url = f'{BASE_URL}/chocolates'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Lista de chocolates:")
        for chocolate_id, chocolate_data in data.items():
            print(f"ID: {chocolate_id}, Tipo: {chocolate_data['chocolate_type']}, Peso: {chocolate_data['peso']}, Sabor: {chocolate_data['taste']}, Relleno: {chocolate_data['filling']}")
    else:
        print("Error al obtener la lista de chocolates.")

# Función para enviar una solicitud POST y agregar un chocolate
def add_chocolate(chocolate_type, peso, taste, filling=None):
    url = f'{BASE_URL}/chocolates'
    data = {
        'chocolate_type': chocolate_type,
        'peso': peso,
        'taste': taste,
        'filling': filling
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        response_data = response.json()
        print("Chocolate agregado exitosamente.")
        print(f"ID asignado: {response_data['chocolate_id']}")
    else:
        print("Error al agregar el chocolate.")

# Función para enviar una solicitud PUT y actualizar un chocolate existente
def update_chocolate(chocolate_id, peso=None, taste=None, filling=None):
    url = f'{BASE_URL}/chocolates/{chocolate_id}'
    data = {}
    if peso:
        data['peso'] = peso
    if taste:
        data['taste'] = taste
    if filling is not None:
        data['filling'] = filling
    
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Chocolate actualizado exitosamente.")
    else:
        print("Error al actualizar el chocolate.")

# Función para enviar una solicitud DELETE y eliminar un chocolate
def delete_chocolate(chocolate_id):
    url = f'{BASE_URL}/chocolates/{chocolate_id}'
    response = requests.delete(url)
    if response.status_code == 200:
        print("Chocolate eliminado exitosamente.")
    else:
        print("Error al eliminar el chocolate.")

# Ejemplo de uso
if __name__ == '__main__':
    # Obtener la lista de chocolates
    get_chocolates()

    # Agregar un nuevo chocolate
    add_chocolate('Tabletas', 100, 'Chocolate negro')

    # Actualizar un chocolate existente (por su ID)
    update_chocolate(1, peso=150, filling='Caramelo')

    # Eliminar un chocolate (por su ID)
    delete_chocolate(2)
