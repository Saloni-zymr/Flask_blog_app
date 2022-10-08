import os
from dotenv import load_dotenv
load_dotenv()


class Config:

    # SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = "salonikothavade01@gmail.com"
    # MAIL_PASSWORD = "dzatovxipxfipiyl"
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
