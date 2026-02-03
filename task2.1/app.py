from flask import Flask,jsonify,request
from extensions import db,migrate
import os
from models import Author,Book
from dotenv import load_dotenv
from schemas import * 
from flask_marshmallow import Marshmallow
from marshmallow.exceptions import ValidationError
from services.user_services import UserService

load_dotenv()
URI = os.getenv("URI")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)


author_schema = Authorschema()
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

@app.route('/authors',methods=['POST'])
def print_all():
    # Create an author
    json_data = request.get_json()
    try:
        author = author_schema.load(json_data)
        name,error = UserService.add_author(name=author['name'],bio=author['bio'])
        if error:
            return jsonify({
                "Error" : error
            }),400
        result = author_schema.dump(name)
        return jsonify({
            "Author Added" : result
        }),200
    except ValidationError as err:
        return jsonify(err.messages),400
    
@app.route('/authors/<id>',methods=['DELETE'])
def delete_author(id):
    deleted_author,error = UserService.delete_auth(id=id)
    if error:
        return jsonify({
            "Error" : error
        }),400

    else :
        return jsonify({
            "Author Delered" : deleted_author
        }),200




if __name__ == '__main__':

    print("hello")
    app.run(debug=True)


