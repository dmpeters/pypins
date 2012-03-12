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
DATABASE_URI = 'sqlite:///./pypins.db'
SECRET_KEY = 'sirl1@$l9oz%x&32l0cv8n0^s9fw8r$!cll5yto0ih_hd+eqs!(y%pypins'
DEBUG_TB_INTERCEPT_REDIRECTS = False
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

class User(Base):
	__tablename__ = 'users'
	id = Column('user_id', Integer, primary_key=True)
	name = Column(String(60))
	oauth_token = Column(String(200))
	oauth_secret = Column(String(200))
	
	def __init__(self, name):
		self.name = name

@app.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@app.after_request
def after_request(response):
	db_session.remove()
	return response

@twitter.tokengetter
def get_twitter_token():
	user = g.user
	if user is not None:
		return user.oauth_token, user.oauth_secret

# Index
@app.route('/')
def index():
    return render_template('index.html')

# Login
@app.route('/login')
def login():
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were signed out')
    return redirect(request.referrer or url_for('index'))

# authorize
@app.route('/oauth-authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    user = User.query.filter_by(name=resp['screen_name']).first()

    if user is None:
        user = User(resp['screen_name'])
        db_session.add(user)

    user.oauth_token = resp['oauth_token']
    user.oauth_secret = resp['oauth_token_secret']
    db_session.commit()

    session['user_id'] = user.id
    flash('You were signed in')
    return redirect(next_url)

# List
@app.route('/<username>')
def list(username):
    username = g.user
    return render_template('list.html')

# Results
@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run()