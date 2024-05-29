from database import db



#candy store
#marca, peso, sabor, origen
#brand, weight, taste, origin

class Candy(db.Model):
    brand__ = "candys"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    taste = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(100), nullable=False)

    def __init__(self, brand, weight, taste, origin):
        self.brand = brand
        self.taste = taste
        self.weight = weight
        self.origin = origin

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Candy.query.all()

    @staticmethod
    def get_by_id(id):
        return Candy.query.get(id)

    def update(self, brand=None, weight=None, taste=None, origin=None):
        if brand is not None:
            self.brand = brand
        if weight is not None:
            self.weight = weight
        if taste is not None:
            self.taste = taste
        if origin is not None:
            self.origin = origin
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
