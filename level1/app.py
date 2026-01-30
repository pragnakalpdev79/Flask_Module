from flask import Flask,jsonify,request

app =Flask(__name__)

#getting all books
@app.route("/books",methods=["GET"])
def get_books():
    books = [
        {"id": 1, "title" : "Flask Guide","Author": "John"},
        {"id":2,"title": "Python Basics" , "Author" : "Jane"}
    ]
    return jsonify({
        "Books" : books
    }),200

#getting a single book by id
@app.route("/books/<int:book_id>",methods=["GET"])
def get_book(book_id):
    book = {
        "id" : book_id,
        "title": "Flask Guide",
        "Author" : "Shreehari"
    }
    return jsonify(book),200 #on success

@app.route("/books",methods=['POST'])
def create_books():
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({
            "error" : "Missing title or author"
        }),400
    new_book = {
        "id" : 123,
        "title" : data['title'],
        "author" : data['author'],
        "publisher" : "pub1"
    } 
    return jsonify({
        "message" : "Book Created",
        "Book" : new_book
    }),201 #on created

@app.route("/books/<int:book_id>",methods=["PUT"])
def update_book_full(book_id):
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({
            "error" : "PUT requires title and author"
        }),400
    
    updated_book = {
        "id" : book_id,
        "title": data["title"],
        "author": data["author"]
    }
    return jsonify({
        "message" : "BOOK REPLACED ",
        "book" : updated_book
    }),200

@app.route("/books/<int:book_id>",methods=["PATCH"])
def update_book_partial(book_id):
    data = request.get_json()
    if not data:
        return jsonify({
            "error" : "No data provided"
        }),400
    existing_book = {
        "id" : book_id,
        "title" : "original title",
        "author" : "original author",
        "year" : 2020
    }
    if 'title' in data:
        existing_book['title'] = data['title']
    if 'author' in data:
        existing_book['author'] = data['author']
    if 'year' in data:
        existing_book["year"] = data["year"]

    return jsonify({
        "message" : "Book Updated!!",
        "book" : existing_book
    }),200

@app.route("/books/<int:book_id>",methods=["DELETE"])
def delete_book(book_id):
    #db.session.delete(book)
    #db.session.commit() if a real app first check
    return jsonify({
        "message" : "Book Deleted successfully"
    }),204

@app.route("/users",methods=['POST'])
def create_users():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    return jsonify({
        "status" : "created",
        "username" : username
    }),201

# pagination and filtering
@app.route('/users',methods=["GET"])
def list_users():
    page = request.args.get("page",1,type=int)
    role = request.args.get("role")
    return jsonify({
        "page" : page,
        "filter_role" : role
    }),200

# BUILDING RESPONSE -- THE OUTPUT
@app.route("/orders",methods=["POST"])
def create_order():
    data = request.get_json()
    if not data or 'item' not in data:
        return jsonify({
            "error" : "Missing item field"
        }),400 # 400 = BAD REQUEST
    return jsonify({
        "id" : 123,
        "status": "penidng"
    }),201


if __name__ == "__main__":
    app.run(debug=True)
