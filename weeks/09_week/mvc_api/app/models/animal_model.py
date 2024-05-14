from database import db


class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")
            db.session.rollback()

    @staticmethod
    def get_all():
        return Animal.query.all()

    @staticmethod
    def get_by_id(id):
        return Animal.query.get(id)

    def update(self, name=None, species=None, age=None):
        try:
            if name is not None:
                self.name = name
            if species is not None:
                self.species = species
            if age is not None:
                self.age = age
            db.session.commit()
        except Exception as e:
            print(f"Error al actualizar en la base de datos: {e}")
            db.session.rollback()

    def delete(self):
        db.session.delete(self)
        db.session.commit()