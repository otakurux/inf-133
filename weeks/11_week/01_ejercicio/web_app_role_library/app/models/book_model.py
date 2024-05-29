from database import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    edition = db.Column(db.String(50), nullable=True)
    availability = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, title, author, edition=None, availability=True):
        self.title = title
        self.author = author
        self.edition = edition
        self.availability = availability

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Book.query.all()

    @staticmethod
    def get_by_id(id):
        return Book.query.get(id)

    def update(self, title=None, author=None, edition=None, availability=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if edition is not None:
            self.edition = edition
        if availability is not None:
            self.availability = availability
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
