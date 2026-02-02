import uuid
import json
import os
import threading
from flask import Flask,jsonify,request
from contextlib import ExitStack
import sys
import time



app =Flask(__name__)
DB_FILE = 'users.json'
busy = threading.Lock() 

def get_data():
    if not os.path.exists(DB_FILE):
        return [] 

    try:
        with open(DB_FILE, 'r') as file:
            content = file.read() #reading from file
            if not content:
                return []
            data = json.loads(content) #converting to dict
            return data.get("users", [])  #returns the list of users
    except Exception as e:
        print(f"Error reading DB: {e}")
        return []
    


def save_data(users_list): #to save users totally from zero
    #start the lock each time some data is written
    animation = "|/-\\"
    i = 0
    while busy.locked() == True:
        print(f"waiting for task to complete")
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        if i == len(animation)-1 :
            i = 0
        i += 1

    with busy:
        try:
            with open(DB_FILE, 'w') as file:
                json.dump({"users": users_list}, file, indent=4)
                print("data saved")
                time.sleep(5)
            return True
        except Exception as e:
            print(f"Error saving DB: {e}")
            return False

def is_valid_uuid(val): #for uuid validation
    try:
        uuid.UUID(val)
        return True
    except ValueError:
        return False




@app.route('/users',methods=["POST"]) # FOR CREATING NEW USERS
def create_users():
    user_data = request.get_json()
    #print("data here:- ",user_data)
    if not user_data: #FIRST CHECKING IF THE BODY IS EMPTY OR NOT
        return jsonify({
            "error" : "The request body is required"
        }),400
    
    required_fields = ["name","email","age"]
    missing = [field for field in required_fields if field not in user_data] #CHECKING MISSING INPUTS 
    if missing: # RETURNING THEM HERE
        return jsonify({
            "error" : f"Missing fields == {missing}"
        }),400
    new_user = {
        "id" : str(uuid.uuid1()),
        "name" : user_data['name'],
        "email" : user_data['email'],
        "age" : user_data['age']
    }

    users = get_data()
    users.append(new_user)
    if save_data(users):
        return jsonify({
            "message": "User created successfully",
            "user": new_user
        }), 201
    else:
        return jsonify({"error": "Internal Server Error"}), 500

    
@app.route("/users", methods=["GET"])
def list_users():
    users = get_data()
    if not users:
        return jsonify({
            "Error" : "No Users Created yet"
        }),404
    return jsonify({"users": users}), 200
    

@app.route("/users/<user_uuid>", methods=["GET"]) # GET SINGLE USER
def get_single_user(user_uuid):
    if not is_valid_uuid(user_uuid):
        return jsonify({"error": "Invalid UUID format"}), 400

    users = get_data()
    for user in users:
        if user["id"] == user_uuid:
            return jsonify(user), 200
            
    return jsonify({"error": "User not found"}), 404
    
@app.route("/users/<uuid>",methods=["PATCH"]) #UPDATE EXISTING USER WITH PATCH REQUEST
def update_user(uuid):
    if not is_valid_uuid(uuid):
        return jsonify({"error": "Invalid UUID format"}), 400
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400
    updates = request.get_json()
    users = get_data()
    user_found = False
    updated_user = {}

    for i,user in enumerate(users):
        if user["id"] == uuid:
            print(users)
            user["name"] = updates.get("name", user["name"]) #default old value if new value is not provided
            user["email"] = updates.get("email", user["email"])
            user["age"] = updates.get("age", user["age"])
            users[i] = user
            updated_user = user
            user_found = True
            print("new:-",users)
            break
    if user_found:
        if save_data(users):
            return jsonify({
                "message": "User updated successfully", 
                "user": updated_user
            }), 200
        else:
            return jsonify({"error": "Internal Server Error"}), 500
    return jsonify({"error": "User not found"}), 404
        
    


@app.route("/users/<uuid>",methods=["DELETE"])
def delete_user(uuid):
    if not is_valid_uuid(uuid):
        return jsonify({"error": "Invalid UUID format"}), 400
    
    users = get_data()
    initial_count = len(users)
    users = [user for user in users if user["id"] != uuid]
    
    if len(users) < initial_count:
        if save_data(users):
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "Internal Server Error"}), 500
        
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
