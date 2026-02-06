from flask import Blueprint,jsonify,request,session,render_template
from flask_jwt_extended import jwt_required,get_jwt_identity,verify_jwt_in_request
import os

home_bp = Blueprint("home",__name__,url_prefix='/home')

@home_bp.route('/',methods=['GET'])
@jwt_required(optional=True)
def home():
    #check if user is logged in or not,(if jwt token or not)
    # if yes render dashboard
    # if no render login page
    os.system('clear')
    print("Checking if jwt exists or not~~~~")
    try:
        loggedin = get_jwt_identity()
        print(loggedin)
        if loggedin:
            print("path-1--jwt exists,user logged in already,loading dashboard")
            return render_template("dashboard.html")
        else:
            print("path-2--jwt does not exists,user not logged in already,loading login page")
            return render_template("login.html")

    except Exception as e:
        print("error path 2")
        return jsonify({
            "eror" : e
        })
    finally:
        print("path-3-in case of other errors,loading,signup page,to start new")
        return  render_template('signup.html')

@home_bp.route('/signup',methods=['POST'])
def signup():
    os.system('clear')
    print("signup request,data submitted!")
    return jsonify({
        "Succes" : "User details submitted"
    })