import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'f217e9ca780ce590618d06ac0f47f118'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    # MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')