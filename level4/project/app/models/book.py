from app.extensions import db
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
import datetime

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # Foreign Key: Links to Author table
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    deleted = db.Column(db.Boolean(),default=False)

    