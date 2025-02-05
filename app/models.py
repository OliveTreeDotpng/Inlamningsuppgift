from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db



class Account(UserMixin, db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(150), nullable=False, unique=True)
    hashed_password = db.Column(db.String(150), nullable=False)
    encrypted_password = db.Column(db.String(150), nullable=False)
