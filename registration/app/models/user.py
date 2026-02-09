from app.extensions import db
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
import datetime

class User(db.Model):
    __tablename__ = 'users'
    registration_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(30), nullable=False) #varchar30
    last_name = db.Column(db.String(30), nullable=False) #varchar 30
    email =  db.Column(db.String(30), nullable=False) #varchar30
    password = db.Column(db.String(256), nullable=False)#varchar 256 --- hash
    address = db.Column(db.String(), nullable=False) #text
    hobbies = db.Column(db.String(50), nullable=False)#varchars 50 store as csv
    gender = db.Column(db.Boolean())#boolean
    deleted = db.Column(db.Boolean(),default=False)
    created_at = db.Column(TIMESTAMP,default=datetime.datetime.now())
    deleted_at = db.Column(TIMESTAMP,default=None)