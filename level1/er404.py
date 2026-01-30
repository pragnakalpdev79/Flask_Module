import uuid
from flask import Flask,jsonify,request

app =Flask(__name__)

users = [
    {"id": "a1b2c3", "name": "Alice"},
    {"id": "d4e5f6", "name": "Bob"}
]
#404 IS USER DOES NOT EXIST
@app.route('/users/<user_id>',methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id),None)
    if not user:
        return jsonify({
            "error" : "User not found"
        }),404
    return jsonify(user),200

#DELETE EXAMPLE
@app.route("/users/<user_id>",methods=['DELETE'])
def delete_user(user_id):
    user = next((u for u in users if u['id'] == user_id),None)
    if not user:
        return jsonify({
            "error" : "User not found"
        }),404
    users.remove(user)
    return jsonify({
        "message" : "User deleted successfully"
    }),200



if __name__ == "__main__":
    app.run(debug=True)
