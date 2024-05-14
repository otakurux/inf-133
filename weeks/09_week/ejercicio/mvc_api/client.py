import requests

BASE_URL = "http://localhost:5000/api"
headers = {"Content-Type": "application/json"}

def create_book(title, author, edition, availability):
    url = f"{BASE_URL}/books"
    book_data = {"title": title, "author": author, "edition": edition, "availability": availability}
    response = requests.post(url, json=book_data, headers=headers)
    return response.json()

def get_books():
    url = f"{BASE_URL}/books"
    response = requests.get(url, headers=headers)
    return response.json()

def get_book_details(book_id):
    url = f"{BASE_URL}/books/{book_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def update_book(book_id, title=None, author=None, edition=None, availability=None):
    url = f"{BASE_URL}/books/{book_id}"
    book_data = {}
    if title is not None:
        book_data["title"] = title
    if author is not None:
        book_data["author"] = author
    if edition is not None:
        book_data["edition"] = edition
    if availability is not None:
        book_data["availability"] = availability
    response = requests.put(url, json=book_data, headers=headers)
    return response.json()

def delete_book(book_id):
    url = f"{BASE_URL}/books/{book_id}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        return f"Libro con ID {book_id} eliminado con éxito."
    else:
        return f"Error: {response.status_code} - {response.text}"

def list_books():
    return [
        {
            "title": "El Principito",
            "author": "Antoine de Saint-Exupéry",
            "edition": 1,
            "availability": 10
        },
        {
            "title": "Cien años de soledad",
            "author": "Gabriel García Márquez",
            "edition": 1,
            "availability": 15
        },
        {
            "title": "Harry Potter y la piedra filosofal",
            "author": "J.K. Rowling",
            "edition": 1,
            "availability": 20
        },
        {
            "title": "Don Quijote de la Mancha",
            "author": "Miguel de Cervantes",
            "edition": 1,
            "availability": 12
        },
        {
            "title": "Moby Dick",
            "author": "Herman Melville",
            "edition": 1,
            "availability": 8
        }
    ]

if __name__ == "__main__":
    print("Creando nuevos libros:")
    books = list_books()
    new_books = [create_book(book["title"], book["author"], book["edition"], book["availability"]) for book in books]
    print(new_books)

    print("\nObteniendo la lista de libros:")
    book_list = get_books()
    print(book_list)

    print("\nObteniendo detalles del libro con ID 1:")
    book_details = get_book_details(1)
    print(book_details)

    print("\nActualizando el libro con ID 1:")
    update_data = {"title": "Cien años de soledad", "author": "Gabriel García Márquez", "edition": 2, "availability": 10}
    updated_book = update_book(1, **update_data)
    print(updated_book)

    print("\nEliminando el libro con ID 1:")
    delete_message = delete_book(1)
    print(delete_message)
