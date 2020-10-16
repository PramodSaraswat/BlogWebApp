import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY='e7b70374bb3711cc41519ddf94418bb5678bf'
	SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'blogdata.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER='smtp.gmail.com'
	MAIL_PORT=465
	MAIL_USE_SSL=True
	MAIL_USERNAME=os.environ.get('EMAIL_USER')
	MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
