from flask import Flask,jsonify,render_template
from app import app
from user.models import User

@app.route('/user/login/', methods=['POST'])
def login():
  return User().login()

@app.route('/user/dashboard/')
def dashboard():
  return render_template('dashboard.html')