from flask import Blueprint, request, jsonify
from models.book_model import Book
from views.book_view import render_book_list, render_book_detail

book_bp = Blueprint("book", __name__)


@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.get_all()
    return jsonify(render_book_list(books))


@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.get_by_id(id)
    if book:
        return jsonify(render_book_detail(book))
    return jsonify({"error": "Libro no encontrado"}), 404


@book_bp.route("/books", methods=["POST"])
def create_book():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")

    if not title or not author or edition is None or availability is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    book = Book(title=title, author=author, edition=edition, availability=availability)
    book.save()

    return jsonify(render_book_detail(book)), 201


@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.get_by_id(id)

    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")

    book.update(title=title, author=author, edition=edition, availability=availability)

    return jsonify(render_book_detail(book))


@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.get_by_id(id)

    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404

    book.delete()
    return jsonify({"message": "Libro eliminado correctamente"}), 200
