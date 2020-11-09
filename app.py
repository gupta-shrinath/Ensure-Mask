from flask import Flask,render_template,session,redirect
from functools import wraps
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'\xdd\xda\xe69\xcd\xcb\x8a6\x96(-\x87\x89\xef\xd4\xe4'
mongoClient = MongoClient('localhost',33017)
db = mongoClient['ensure-mask']


def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            redirect('/')
    return wrap

from user import routes

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

