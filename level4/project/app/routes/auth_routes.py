from flask import Blueprint,jsonify,request
from app.models.author import Author
from app.schemas.author import Authorschema
from app.schemas.book import Bookschema 
from app.services.author_services import AuthorService
from app.services.book_services import BookService
from marshmallow.exceptions import ValidationError
import os



auth_bp = Blueprint("authors",__name__,url_prefix='/api/v1/authors')
author_schema = Authorschema()
book_schema = Bookschema()


#===============================================================================
#2.1 ENDPOINT TO CREATE AN AUTHOR
@auth_bp.route('/',methods=['POST'])
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
#2.3 ENDPOINT TO GET AUTHOR WITH BOOK
@auth_bp.route('/<int:id>',methods=['GET'])
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
#2.5 ENDPOINT TO DELETE THE AUTHORS
@auth_bp.route('/<int:id>',methods=['DELETE'])
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
