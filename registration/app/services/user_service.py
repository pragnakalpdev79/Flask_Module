from app.extensions import db
from sqlalchemy import update
import os 
import jwt
from flask import Flask, jsonify, request
from app.models.user import User 
from flask_jwt_extended import ( create_access_token, create_refresh_token, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies)
from datetime import datetime,timezone,timedelta
import hashlib
import app

class UserService:

    @staticmethod
    def user_signup(user_details):
        for i in user_details:
            if not i:
                return None,"Invalid Input"
        if len(user_details) != 8:
            return None,"Invalid Input request"
        if user_details[3] != user_details[4]:
            #passwords do not match
            return None,"Passwords do not match"
        if User.query.filter_by(email=user_details[2]).first():
            return None,"User already registerd,please log in"
        if user_details[6] == 'male':
            gender = False
        if user_details[6] == 'female':
            gender = True
        passw = user_details[3]
        phash = (hashlib.md5(passw.encode('utf-8'))).hexdigest()
        phash = str(phash)
        new_user = User(first_name=user_details[0],
                        last_name=user_details[1],
                        email=user_details[2],
                        password = phash,
                        address=user_details[7],
                        hobbies=user_details[6],
                        gender=gender)
        db.session.add(new_user)
        db.session.commit()
        return new_user,None


    @staticmethod
    def user_login(email,password):
        user = User.query.filter_by(email=email,deleted=False).first()
        #print(user.email)
        if not user:
            return None,"User Does not exists,please sign up!"
        phash = (hashlib.md5(password.encode('utf-8'))).hexdigest()
        phash = str(phash)
        upass = user.password
        uphash = (hashlib.md5(upass.encode('utf-8'))).hexdigest()
        if not phash == upass:
            return None,"Wrong Password Please try again"
        return user,None