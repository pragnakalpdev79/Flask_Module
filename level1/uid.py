import uuid
from flask import Flask,jsonify,request

app =Flask(__name__)

@app.route('/users/<user_id>',methods=["GET"])
def get_user(user_id):
    try:
        uuid.UUID(user_id)
    except ValueError:
        return jsonify({
            "error" : "Invalid UUID format"
        }),400
    
    user = {"id" : user_id, "name" : "Alice"}
    return jsonify(user) ,200




if __name__ == "__main__":
    app.run(debug=True)
