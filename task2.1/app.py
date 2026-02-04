from flask import Flask,jsonify,request
from extensions import db,migrate
import os
from models import Author,Book
from dotenv import load_dotenv
from schemas import * 
from flask_marshmallow import Marshmallow
from marshmallow.exceptions import ValidationError
from services.author_service import AuthorService
from services.book_services import BookService

load_dotenv()
URI = os.getenv("URI")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)


author_schema = Authorschema()
book_schema = Bookschema()
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

#===============================================================================
#2.1 ENDPOINT TO CREATE AN AUTHOR
@app.route('/authors',methods=['POST'])
def create_author():
    # Create an author
    json_data = request.get_json()
    try:
        #validating the json request with author schema
        author = author_schema.load(json_data)
        #then passing it to add author service
        name,error = AuthorService.add_author(name=author['name'],bio=author['bio'])
        if error:
            return jsonify({
                "Error" : error
            }),400
        result = author_schema.dump(name)
        return jsonify({
            "Author Added" : result
        }),200
    except ValidationError as err: #if the input is incorrect the marshmallow will throw the error here
        return jsonify(err.messages),400
#===============================================================================
#2.2 ENDPOINT TO CREATE A BOOK
@app.route('/books',methods=['POST'])
def create_book():
    # Create a book
    json_data = request.get_json()
    try:
        #validating the json request with book schema
        book = book_schema.load(json_data)
        #then passing it to add author service
        name,error = BookService.add_book(title=book['title'],price=book['price'],author_id=book['author_id'])
        if error:
            return jsonify({
                "Error" : error
            }),400
        result = book_schema.dump(name)
        return jsonify({
            "Book Added" : result
        }),200
    except ValidationError as err: #if the input is incorrect the marshmallow will throw the error here
        return jsonify(err.messages),400
#===============================================================================
#2.3 ENDPOINT TO GET AUTHOR WITH BOOK
@app.route('/authors/<int:id>',methods=['GET'])
def author_list(id):
    os.system('clear')
    author,error  = AuthorService.get_author_books(id)
    if error:
        return jsonify({
            "Error" : error
        })
    #author_books = [i for i in UserService.get_books(id)]
    books,error = BookService.get_books(id)
    if error:
        return jsonify({
            "Error" : error
        })
    book_list = [book_schema.dump(i) for i in books]
    #print("main books",book_list)
    result= author_schema.dump(author)
    result.update({"books":book_list}) 
    result.update({"id":id}) 
    print(result)
    return result
#===============================================================================
#2.4 ENDPOINT TO UPDATE BOOK PRICE WITH ID
@app.route('/books/<int:id>',methods=['PUT'])
def update_price(id):
    json_data = request.get_json()
    new_price = json_data['price']
    if not new_price:
        return jsonify({
         "Something went wrong" : "Error" 
        })
    book_price,error = BookService.update_book_price(id,new_price)
    if error:
        return jsonify({
            "Error" : error
        })
    return jsonify({
         "New price is" : book_price
    })
#===============================================================================
#2.5 ENDPOINT TO DELETE THE AUTHORS
@app.route('/authors/<int:id>',methods=['DELETE'])
def delete_author(id):
    deleted_author,error = AuthorService.delete_auth(id)
    if error:
        return jsonify({
            "Error" : error
        }),400
    else :
        return jsonify({
            "Author Deleted" : deleted_author
        }),200




if __name__ == '__main__':

    print("hello")
    app.run(debug=True)


