from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Skapar en instans av SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # Skapar databasen i minnet
    app.config["SECRET_KEY"] = "you-will-never-guess-this-key" # Säkerhetsnyckel 

    db.init_app(app) # Initierar databasen
    
    with app.app_context(): # Skapa appens kontext
        from . import routes # Importera routes.py
        db.create_all() # Skapa databasen
    
    return app