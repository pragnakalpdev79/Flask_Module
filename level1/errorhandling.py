from flask import Flask,jsonify,request
import json

app = Flask(__name__)

@app.route("/products/<int:product_id>",methods=["GET"])
def get_product(product_id):
    # error-1 validating if product id is positive
    if product_id <= 0:
        return jsonify({
            "error" : "INvalid product ID"
        }),400
    # error-2 load products from file
    try:
        with open("inventory.json","r") as f:
            data = json.load(f)
            products = data.get("products",[])
    except FileNotFoundError:
        return jsonify({
            "error" : "Internal Server Errror"
        }),500
    except json.JSONDecodeError:
        return jsonify({
            "error" : "Internal Server Error"
        }),500
    # error - 3 product not found
    product = next((p for p in products if p['id'] == product_id),None)
    if not product:
        return jsonify({
            "error" : "product not found"
        }),404
    
    return jsonify(product),200

@app.route("/products",methods=["POST"])
def create_product():
    data = request.get_json()

    #error-1 no data
    if not data:
        return jsonify({
            "error" : "Request Body Required"
        }),400
    
    # error-2 missing required fields
    if 'name' not in data or 'praise' not in data:
        return jsonify({
            "error" : "Missing name or price"
        }),400
    
    #error-3 invalid data type
    if not isinstance(data['price'],(int,float)) or data['price'] < 0:
        return jsonify({
            "error" : "price must be a positive number"
        }),400
    
    new_product = {
        "id" : 123,
        "name" : data['name'],
        "price" : data["price"]
    }
    return jsonify(new_product) , 201
    
