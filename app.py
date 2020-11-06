from flask import Flask,render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost',33017)
db = client['ensure-mask']

from user import routes
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

