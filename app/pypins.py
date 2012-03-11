from flask import Flask, request, redirect, url_for, session, flash, g, render_template
from flaskext.oauth import OAuth

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# configuration
# DATABASE_URI = 'PATH_TO_DATABASE'
SECRET_KEY = 'development key'
DEBUG = True

# setup flask
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()