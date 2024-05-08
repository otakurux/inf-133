from database import db


# Define la clase `Book` que hereda de `db.Model`
# `Book` representa la tabla `Books` en la base de datos
class Book(db.Model):
    __tablename__ = "books"

    # Define las columnas de la tabla `Books`
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    edition = db.Column(db.Integer(100), nullable=False)
    availability = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Book`
    def __init__(self, title, author, edition, availability):
        self.title = title
        self.author = author
        self.edition = edition
        self.availability = availability

    # Guarda un Book en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Bookes de la base de datos
    @staticmethod
    def get_all():
        return Book.query.all()

    # Obtiene un Book por su ID
    @staticmethod
    def get_by_id(id):
        return Book.query.get(id)

    # Actualiza un Book en la base de datos
    def update(self, title=None,author=None, edition=None, availability=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if edition is not None:
            self.edition = edition
        if availability is not None:
            self.availability = availability
        db.session.commit()

    # Elimina un Book de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()