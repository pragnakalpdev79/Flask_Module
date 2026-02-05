from app.extensions import db
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
import datetime

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False) #Name must be unique
    bio = db.Column(db.String(500))
    deleted = db.Column(db.Boolean(),default=False)
    created_at = db.Column(TIMESTAMP,default=datetime.datetime.now())
    deleted_at = db.Column(TIMESTAMP,default=None)
    # One-to-Many: One author has many books
    books = db.relationship('Book', backref='author')

    