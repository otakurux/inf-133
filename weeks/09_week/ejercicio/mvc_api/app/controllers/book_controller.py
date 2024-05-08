from flask import Blueprint, request, jsonify
from models.book_model import book
from views.book_view import render_book_list, render_book_detail

# Crear un blueprint para el controlador de bookes
book_bp = Blueprint("book", __name__)


# Ruta para obtener la lista de bookes
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = book.get_all()
    return jsonify(render_book_list(books))


# Ruta para obtener un book específico por su ID
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = book.get_by_id(id)
    if book:
        return jsonify(render_book_detail(book))
    return jsonify({"error": "book no encontrado"}), 404


# Ruta para crear un nuevo book
@book_bp.route("/books", methods=["POST"])
def create_book():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition =data.get("edition")
    availability = data.get("availability")

    # Validación simple de datos de entrada
    if not title or not author or availability or edition is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo book y guardarlo en la base de datos
    book = book(title=title, author=author, edition=edition, availability=availability)
    book.save()

    return jsonify(render_book_detail(book)), 201


# Ruta para actualizar un book existente
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = book.get_by_id(id)

    if not book:
        return jsonify({"error": "book no encontrado"}), 404

    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")

    # Actualizar los datos del book
    book.update(title=title, author=author, edition=edition, availability=availability)

    return jsonify(render_book_detail(book))


@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = book.get_by_id(id)

    if not book:
        return jsonify({"error": "book no encontrado"}), 404
    book.delete()

    return "", 204