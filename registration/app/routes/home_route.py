from flask import Blueprint,jsonify,request,session,render_template,redirect,url_for,flash,make_response
from flask_jwt_extended import jwt_required,get_jwt_identity,verify_jwt_in_request, set_access_cookies,set_refresh_cookies, create_refresh_token,create_access_token,unset_jwt_cookies
import os
import csv
import io
import jwt
import requests
from app.services.user_service import UserService
from app.schemas.user import UserSchema


home_bp = Blueprint("home",__name__,url_prefix='/home')
user_schema = UserSchema()

@home_bp.route('/',methods=['GET'])
def home():
    if request.method=='GET':
        loggedin = request.cookies.get('access_token_cookie')
        if loggedin:
            return redirect(url_for('home.dashboard'))
    return render_template('root.html')

@home_bp.route('/dashboard',methods=['GET','POST'])
@jwt_required()
def dashboard():
    #os.system('clear')
    print("Checking if jwt exists or not~~~~")
    print()
    #check if user is logged in or not,(if jwt token or not)
    loggedin = get_jwt_identity()
    # if yes render dashboard
    # if no render login page
    print("hello",loggedin)
    if not loggedin:
        #log in not a success
        print(loggedin)
        return redirect(url_for('home.login'))
    payload =  requests.get("https://icanhazdadjoke.com/",headers={"Accept": "text/plain"})
    print(payload.content)
    joke = payload.content.decode()
    return render_template('dashboard.html',joke=joke,email=loggedin)

@home_bp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        os.system('clear')
        print("signup page loading")
        return render_template('signup.html')
    os.system('clear')
    hobbl = []
    usel = []
    print("signup request,data submitted!")
    for formf,data in request.form.items():
        if formf == "hobbies" :
            continue
        #print(formf,data)
        usel.append(data)
    hobbl = request.form.getlist("hobbies")
    result = io.StringIO()
    writer = csv.writer(result)
    writer.writerow(hobbl)
    hobb_csv = result.getvalue()
    #print(hobb_csv)
    #print(hobbl)
    #calling signup servcie to feed the data into db
    usel.append(hobb_csv)
    usel.pop(7)
    #usel.append(addr)
    print(usel)
    print(len(usel)) 
    
    user,error = UserService.user_signup(user_details=usel)
    if error:
        flash(error)
        return redirect(url_for('home.home'))
    #['Shreehari', 'Kadia', 'shreeharikadia@gmail.com', 'Pass@123', 'Pass@123', 'male', 'music,dance,badminton\r\n']
    userr = user_schema.dump(user)
    flash("Your Acount has been created,please log in now")
    return redirect(url_for('home.home'))

@home_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        loggedin = request.cookies.get('access_token_cookie')
        print(loggedin)
        if loggedin:
            return redirect(url_for('home.dashboard'))
        #os.system('clear')
        print("login page loading")
        return render_template('login.html')
    #if request is post
    email = request.form.get('email')
    password = request.form.get("password")
    if not email and password: #if by any chancev we recivew a bad request
        flash("Please completed the required fields")
        return redirect(url_for('home.login'))
    user,error = UserService.user_login(email=email,password=password)
    if error :
        flash(error)
        return redirect(url_for('home.login'))
    #os.system('clear')
    print("===========================================")
    #print(name['access_token'])
    print(user.email)
    access_token_cookie = create_access_token(identity=user.email) #creates an encoded access token
    #refresh_token = create_refresh_token(identity=user.email)
    print(access_token_cookie) #access_token

    if access_token_cookie:
        print("generated!!")
    resp = make_response(redirect(url_for('home.dashboard')))

    #resp.set_cookie("access_token_cookie",access_token_cookie)
    set_access_cookies(resp,access_token_cookie)
    resp.set_cookie("email",user.email)
    resp.headers['content-type'] = 'application/json'
    
    #set_refresh_cookies(resp,refresh_token)
    print(resp)
    return resp
    
@home_bp.route('/logout',methods=['GET','POST'])
def logout():
    resp = make_response(redirect(url_for('home.home')))
    resp.set_cookie('access_token_cookie', expires=0)
    resp.set_cookie('emails', expires=0)
    unset_jwt_cookies(resp)
    return resp


    




