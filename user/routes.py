from flask import render_template,redirect
from app import app,login_required
from user.models import User
from app import oauth

@app.route('/user/login/', methods=['POST'])
def login():
  return User().login()

@app.route('/user/register/', methods=['POST'])
def register():
  return User().register()

@app.route('/user/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/user/logout/')
def logout():
  return User().logout()

@app.route('/user/google/')
@login_required
def social():
  return User().google_social()

@app.route('/user/google/auth/')
def google_auth():
  return User().google_auth()

@app.route('/user/twitter/')
def twitter():
  return User().twitter_social()

@app.route('/user/twitter/auth/')
def twitter_auth():
  return User().twitter_auth()

@app.route('/user/facebook/')
def facebook():
  return User().facebook_social()

@app.route('/user/facebook/auth/')
def facebook_auth():
  return User().facebook_auth()
