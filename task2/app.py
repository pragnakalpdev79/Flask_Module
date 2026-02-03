import json
from flask import Flask,jsonify,request
from extensions import db,migrate
from models import Book #for migrations to detect the models
from service.user_service import UserService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #flask internal config setting parameters
db.init_app(app) 
migrate.init_app(app,db)





