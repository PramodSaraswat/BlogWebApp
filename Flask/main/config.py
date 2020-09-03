import os

class Config:
    SECRET_KEY='e7b70374bb3711cc41519ddf94418bb5678bf'
    SQLALCHEMY_DATABASE_URI='sqlite:///blogdata.db'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
