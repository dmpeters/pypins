from flask import Flask, request, redirect, url_for, session, flash, g, render_template
from flaskext.oauth import OAuth
from flask_debugtoolbar import DebugToolbarExtension

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# configuration
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(
    # debug
    DEBUG=True,

	# database
	DATABASE_URI = 'PATH_TO_DATABASE',

    # Secret Key
    SECRET_KEY = 'SECRET_KEY'
)
toolbar = DebugToolbarExtension(app)
oauth = OAuth()


# The Twitter
twitter = oauth.remote_app('twitter',
	base_url='http://api.twitter.com/1/',
	request_token_url='http://api.twitter.com/oauth/request_token',
	access_token_url='http://api.twitter.com/oauth/access_token',
	authorize_url='http://api.twitter.com/oauth/authenticate',
	consumer_key='TWITTER_KEY',
	consumer_secret='TWITTER_SECRET'
)

# setup sqlalchemy
# engine = create_engine(DATABASE_URI)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
# 
# 
# def init_db():
#     Base.metadata.create_all(bind=engine)


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