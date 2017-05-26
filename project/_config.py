import os

#grab folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
"""The WTF_CSRF_ENABLED config setting is used for cross-site request	
forgery prevention, which makes your app more secure.
The SECRET_KEY config setting is used in conjunction with the 
WTF_CSRF_ENABLED setting in	order to create	a cryptographic	token 
that is	used to	validate a form. It's also used	for	the	same reason	in 
conjunction	with sessions"""
CSRF_ENABLED = True
SECRET_KEY = "can'tguessthis"

#define the full path for the databae
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database URI
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH