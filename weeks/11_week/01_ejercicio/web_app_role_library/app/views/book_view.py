from flask import render_template
from flask_login import current_user


def list_books(books):
    return render_template(
        "books.html",
        books=books,
        title="Lista de bookes",
        current_user=current_user,
    )

def create_book():
    return render_template(
        "create_book.html", title="Crear Book", current_user=current_user
    )

def update_book(book):
    return render_template(
        "update_book.html",
        title="Editar Book",
        book=book,
        current_user=current_user,
    )
