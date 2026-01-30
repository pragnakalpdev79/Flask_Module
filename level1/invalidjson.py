import uuid
from flask import Flask,jsonify,request

app =Flask(__name__)

@app.route('/users',methods=["POST"])
def create_user(user_id):
    try:
        data = request.get_json()
    except Exception:
        return jsonify({
            "error" : "Invalid JSON"
        }),400
    if not data:
        return jsonify({
            "error" : "Request Body is required"
        }),400
    return jsonify({
        "message": "user created"
    }),201
  


if __name__ == "__main__":

    app.run(debug=True)
