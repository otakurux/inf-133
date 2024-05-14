from flask import Flask
from controllers.book_controller import book_bp
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(book_bp, url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)