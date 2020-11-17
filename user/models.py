from flask import Flask,request,redirect,jsonify,session,url_for
from app import db
from passlib.hash import pbkdf2_sha256
import uuid
from app import oauth,app
import urllib.request
import os

class User:
    def login(self):
        print(request.form)
        user = db.users.find_one({
            'email':request.form.get('email')
        })
        password = request.form.get('password')
        print(user)
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

    def google_social(self):
        redirect_uri = url_for('google_auth', _external=True)
        return oauth.google.authorize_redirect(redirect_uri)

    def google_auth(self):
        token = oauth.google.authorize_access_token()
        user = oauth.google.parse_id_token(token)
        print(user.picture)
        self.download_image(user.picture,'google')
        return redirect('/user/dashboard/')
    
    def twitter_social(self):
        redirect_uri = url_for('twitter_auth', _external=True)
        return oauth.twitter.authorize_redirect(redirect_uri)

    def twitter_auth(self):
        token = oauth.twitter.authorize_access_token()
        resp = oauth.twitter.get('account/verify_credentials.json')
        profile = resp.json()
        print(profile['profile_image_url'])
        self.download_image(profile['profile_image_url'],'twitter')
        # do something with the token and profile
        return redirect('/user/dashboard/')
    
    
    def facebook_social(self):
        redirect_uri = url_for('facebook_auth', _external=True)
        return oauth.facebook.authorize_redirect(redirect_uri)


    def facebook_auth(self):
        token = oauth.facebook.authorize_access_token()
        resp = oauth.facebook.get(
        'https://graph.facebook.com/me?fields=picture{url}')
        profile = resp.json()
        # do something with the token and profile
        print(profile['picture']['data']['url'])
        self.download_image(profile['picture']['data']['url'],'facebook')
        return redirect('/user/dashboard/')

    def download_image(self,image_url,provider):
        user_id = session.get('user')["_id"]
        print(user_id)
        save_location = 'citizens/' + user_id + '/' + provider + '.jpg'
        urllib.request.urlretrieve(image_url,save_location)

    def save_photo(self):
        print(request.files)
        face_img_one = request.files["photoOne"]
        face_img_two = request.files["photoTwo"]
        face_img_three = request.files["photoThree"]
        user_id = session.get('user')["_id"]
        save_location = app.config['USER_IMAGE_UPLOADS'] + user_id
        face_img_one_ext = face_img_one.filename.rsplit(".", 1)[1]
        print(face_img_one.filename,face_img_one_ext)
        face_img_one.save( os.path.join(save_location,'face-1.' + face_img_one_ext) )
        face_img_two_ext = face_img_two.filename.rsplit(".", 1)[1]
        face_img_two.save( os.path.join(save_location,'face-2.' + face_img_two_ext) )
        face_img_three_ext = face_img_three.filename.rsplit(".", 1)[1]
        face_img_three.save( os.path.join(save_location,'face-3.' + face_img_three_ext) )