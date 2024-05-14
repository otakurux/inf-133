from database import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    def __init__(self, first_name, last_name, email, password, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.dob = dob

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    def update(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
