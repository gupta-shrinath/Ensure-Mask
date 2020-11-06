from flask import Flask,request,redirect,jsonify
from app import db
class User:
    def login(self):
        print(request.form)
        email = request.form.get('email')
        password = request.form.get('password')
        if db.users.find_one({"email":email,"password":password}):
            print('User Exist')
            return jsonify({"status":"Success"}), 200
        else:
            print("User doesnot EXIST")
            return jsonify({ "error": "Invalid login credentials" }), 401
       
