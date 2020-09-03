from main.config import Config
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
mail=Mail(app)

from main import routes
from main.errors.handlers import errors
app.register_blueprint(errors)
