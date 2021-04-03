"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))



class config(object):
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')


class ProductionConfig(config):

    DEBUG = False
    TESTING = False


class DevelopmentConfig(config):
    
    DEBUG = True
    TESTING = True
