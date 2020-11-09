from flask import Flask,request,redirect,jsonify,session
from app import db
from passlib.hash import pbkdf2_sha256
import uuid

class User:
    def login(self):
        print(request.form)
        user = db.user.find_one({
            'email':request.form.get('email')
        })
        password = request.form.get('password')
        if user and pbkdf2_sha256.verify(password,user['password']):
            print('User Exist')
            self.start_session(user)
            return jsonify({"status":"Success"}), 200
        else:
            print("User doesnot EXIST")
            return jsonify({ "error": "Invalid login credentials" }), 401
       
    def register(self):
        user = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get('userName'),
            "email" : request.form.get('userEmail'),
            "mobile" : request.form.get('userMobile'),
            "address" : request.form.get('userAddress'),
            "pincode" : request.form.get('userPincode'),
            "password" : request.form.get('userPassword')
        }
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        print(user)
        if db.users.find_one({"email":user['email']}):
            return jsonify({'error':'User exists !'}), 400
        
        if db.users.insert_one(user):
            return jsonify(user),200
        
        return jsonify({'error':'Register Failed !'}),400
    
    def start_session(self,user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user

    def logout(self):
        session.clear()
        return redirect('/')