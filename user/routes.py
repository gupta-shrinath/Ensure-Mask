from flask import render_template
from app import app,login_required
from user.models import User

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

