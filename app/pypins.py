import sys
# so we can include the pypins package in the search path
sys.path.append("../")

from flask import Flask, request, redirect, url_for, session, flash, g, render_template
from flaskext.oauth import OAuth
from flask_debugtoolbar import DebugToolbarExtension

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# configuration
DATABASE_URI = 'sqlite:///../pypins.db'
SECRET_KEY = 'sirl1@$l9oz%x&32l0cv8n0^s9fw8r$!cll5yto0ih_hd+eqs!(y%pypins'
DEBUG=True

# flask
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
toolbar = DebugToolbarExtension(app)
oauth = OAuth()

# The Twitter
twitter = oauth.remote_app('twitter',
	base_url='http://api.twitter.com/1/',
	request_token_url='http://api.twitter.com/oauth/request_token',
	access_token_url='http://api.twitter.com/oauth/access_token',
	authorize_url='http://api.twitter.com/oauth/authenticate',
	consumer_key='YoreesqTapnna5BAxFLW7A',
	consumer_secret='ofaemfTp6qdHjaOSSqF5EvWuw7C46wCwzvAr0nwhc'
)

# sqlalchemy
engine = create_engine(DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)


# Index
@app.route('/')
def index():
    return render_template('index.html')


# Login
@app.route('/login')
def login():
    return render_template('login.html')


# List
@app.route('/list')
def list():
    return render_template('list.html')


# Results
@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run()