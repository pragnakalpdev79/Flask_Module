from flask import Blueprint,jsonify,request
from app.schemas.book import Bookschema 
from marshmallow.exceptions import ValidationError
from app.services.book_services import BookService
book_bp = Blueprint("books",__name__,url_prefix='/books')
book_schema = Bookschema()

#===============================================================================
#2.2 ENDPOINT TO CREATE A BOOK
@book_bp.route('/',methods=['POST'])
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
#2.4 ENDPOINT TO UPDATE BOOK PRICE WITH ID
@book_bp.route('/<int:id>',methods=['PUT'])
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

