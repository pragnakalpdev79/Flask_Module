import uuid
import json
import os
from flask import Flask,jsonify,request

app =Flask(__name__)

@app.route('/users',methods=["POST"]) # FOR CREATING NEW USERS
def create_users():
    
    user_data = request.get_json()
    inputs = ["name","email","age"]
    missing = []
    #print("data here:- ",user_data)
    if not user_data: #FIRST CHECKING IF THE BODY IS EMPTY OR NOT
        return jsonify({
            "error" : "The request body is required"
        }),400
    for i in inputs: #CHECKING MISSING INPUTS 
        if i not in user_data:
            missing.append(i)
    if missing: # RETURNING THEM HERE
        return jsonify({
            "error" : f"Missing fields == {missing}"
        }),400
    id = uuid.uuid1()
    user = {
        "id" : str(id),
        "name" : user_data['name'],
        "email" : user_data['email'],
        "age" : user_data['age']

    }
    try:
        if not os.path.exists('users.json'): #CREATES A FILE IF IT DOES NOT EXIST ALREADY
            with open('users.json','w') as file:
                file.write('[]')
        with open('users.json','r+') as u:
            data = json.load(u)
            #print("ADDING A NEW USER:-",data)
            data["users"].append(user)
            u.seek(0)
            json.dump(data,u,indent=4)
    except:
        return jsonify({
            "error" : "Internal Server Error"
        }),500

    return jsonify({
        "message" : "User Created Successfully",
        "user" : user
    }),201

@app.route("/users",methods=["GET"])
def list_users():
    if not os.path.exists('users.json'):
        return jsonify({
            "Error" : "No Users Created yet"
        }),404
    try:
        with open('users.json','r') as u:
            data = json.load(u)
            return jsonify({
                "users" : data["users"]
            })
    except: 
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    
@app.route("/users/<uuid>",methods=["GET"])
def list_users():
    if not os.path.exists('users.json'):
        return jsonify({
            "Error" : "No Users Created yet"
        }),404
    try:
        with open('users.json','r') as u:
            data = json.load(u)
            try:
                
    except: 
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    





if __name__ == "__main__":
    app.run(debug=True)
