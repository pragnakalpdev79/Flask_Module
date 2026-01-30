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
def single_user(uuid):
    if not os.path.exists('users.json'):
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    try:
        with open('users.json','r') as u:
            data = json.load(u)
            if not data or not data["users"]:
                return jsonify({
                    "Error" : "No users created yet"
                }),404
            for i in data["users"]:
                if i["id"] == uuid:
                    return i
            return ({
                "Error" : "User not found"
            })
    except: 
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    
@app.route("/users/<uuid>",methods=["PATCH"])
def update_user(uuid):
    if not os.path.exists('users.json'):
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    try:
        with open('users.json','r+') as u:
            data = json.load(u)
            requested_user = request.get_json()

            if not data or not data["users"]:
                return jsonify({
                    "Error" : "No users created yet"
                }),404
            index = 0
            for user in data["users"]:
                print("entered the loop",str(user["id"]) == uuid,not requested_user )
                if str(user["id"]) == uuid and requested_user: 
                    #user matched and the body is not empty
                    print("entered the loop and passed the condition")
                    print("Old user base :- \n=======================================================================")
                    for j in data["users"]:
                        print(j)
                    #print(data["users"])
                    user = {key : requested_user[key] if key in requested_user else user[key] for key in user}
                    u.seek(0)
                    #print(user)
                    data["users"][index] = user
                    print("Updated user base :-\n============================================================ ")
                    #print(data["users"])
                    for j in data["users"]:
                        print(j)
                    json.dump({"users":data["users"]},u,indent=4)
                    return jsonify({
                        "message" : "User Updated Successfully",
                        "user" : user
                    })
                index += 1

            return ({
                "Error" : "User not found",
                "type" : f"{type(uuid)}",
                "req_user" : f"{requested_user}"
            })
    except: 
        return jsonify({
            "Error" : "Internal Server Error"
        }),500

@app.route("/users/<uuid>",methods=["DELETE"])
def delete_user(uuid):
    if not os.path.exists('users.json'):
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    try:
        with open('users.json','r+') as u:
            data = json.load(u)
            requested_user = request.get_json()

            if not data or not data["users"]:
                return jsonify({
                    "Error" : "No users created yet"
                }),404
            for user in data["users"]:
                print("entered the loop",str(user["id"]) == uuid,not requested_user )
                if str(user["id"]) == uuid and requested_user: 
                    #user matched and the body is not empty
                    print("entered the loop and passed the condition")
                    user = {key : requested_user[key] if key in requested_user else user[key] for key in user}
                    return jsonify({
                        "message" : "User Updated Successfully",
                        "user" : user
                    })

            return ({
                "Error" : "User not found",
                "type" : f"{type(uuid)}",
                "req_user" : f"{requested_user}"
            })
    except: 
        return jsonify({
            "Error" : "Internal Server Error"
        }),500
    
if __name__ == "__main__":
    app.run(debug=True)
