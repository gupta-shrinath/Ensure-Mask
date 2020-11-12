from flask import Flask,render_template,session,redirect
from functools import wraps
from pymongo import MongoClient
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET')
app.config['SERVER_NAME'] = 'localhost:5000'
# Database Config
mongoClient = MongoClient('localhost',33017)
db = mongoClient['ensure-mask']

# Google Oauth Config
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name = 'google',
    client_id = GOOGLE_CLIENT_ID,
    client_secret = GOOGLE_CLIENT_SECRET,
    server_metadata_url = CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

# Twitter Oauth Config
TWITTER_CLIENT_ID = os.environ.get('TWITTER_CLIENT_ID')
TWITTER_CLIENT_SECRET = os.environ.get('TWITTER_CLIENT_SECRET')
oauth.register(
    name='twitter',
    client_id = TWITTER_CLIENT_ID,
    client_secret = TWITTER_CLIENT_SECRET,
    request_token_url = 'https://api.twitter.com/oauth/request_token',
    request_token_params = None,
    access_token_url = 'https://api.twitter.com/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://api.twitter.com/oauth/authenticate',
    authorize_params = None,
    api_base_url = 'https://api.twitter.com/1.1/',
    client_kwargs = None,
)

# Facebook Oauth Config
FACEBOOK_CLIENT_ID = os.environ.get('FACEBOOK_CLIENT_ID')
FACEBOOK_CLIENT_SECRET = os.environ.get('FACEBOOK_CLIENT_SECRET')
oauth.register(
    name='facebook',
    client_id = FACEBOOK_CLIENT_ID,
    client_secret = FACEBOOK_CLIENT_SECRET,
    access_token_url = 'https://graph.facebook.com/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://www.facebook.com/dialog/oauth',
    authorize_params = None,
    api_base_url = 'https://graph.facebook.com/',
    client_kwargs={'scope': 'email'},
)

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

