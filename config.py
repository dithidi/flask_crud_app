from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY', 'dev')
    basedir = path.abspath(path.dirname(__file__))

    DEBUG = environ.get('DEBUG_MODE', False)
    TESTING = environ.get('TESTING_MODE', False)
    CSRF_ENABLED = environ.get('CSRF_ENABLED', True)

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE="filesystem"
