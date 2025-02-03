from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SECRET_KEY"] = "you-will-never-guess-this-key"

    db.init_app(app)
    
    with app.app_context(): # Skapa appens kontext
        from app import routes # Importera routes.py
        db.create_all() # Skapa databasen
    
    return app