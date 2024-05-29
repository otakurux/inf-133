from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.book_model import Book  # Asegúrate de que la ruta a tu modelo sea correcta
from views import book_view

from utils.decorators import role_required

book_bp = Blueprint("book", __name__)


@book_bp.route("/books")
@login_required
def list_books():
    books = Book.get_all()
    return book_view.list_books(books)


@book_bp.route("/books/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_book():
    if request.method == "POST":
        if current_user.has_role("admin"):
            title = request.form["title"]
            author = request.form["author"]
            edition = request.form.get("edition")
            availability = request.form["availability"] == 'true'
            book = Book(title=title, author=author, edition=edition, availability=availability)
            book.save()
            flash("Libro creado exitosamente", "success")
            return redirect(url_for("book.list_books"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return book_view.create_book()


@book_bp.route("/books/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_book(id):
    book = Book.get_by_id(id)
    if not book:
        return "Libro no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            title = request.form["title"]
            author = request.form["author"]
            edition = request.form.get("edition")
            availability = request.form["availability"] == 'true'
            book.update(title=title, author=author, edition=edition, availability=availability)
            flash("Libro actualizado exitosamente", "success")
            return redirect(url_for("book.list_books"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return book_view.update_book(book)


@book_bp.route("/books/<int:id>/delete")
@login_required
@role_required("admin")
def delete_book(id):
    book = Book.get_by_id(id)
    if not book:
        return "Libro no encontrado", 404
    if current_user.has_role("admin"):
        book.delete()
        flash("Libro eliminado exitosamente", "success")
        return redirect(url_for("book.list_books"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
