import os

class Config:
    '''
    Describes the general configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/discourse'
    QUOTE_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # emails configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):

    '''
    Production configuration child class
    Args:
        Coanfig: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    

class TestConfig(Config):

    '''
    Test configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/discourse'


class DevConfig(Config):

    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/discourse'
    DEBUG = True
    
    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}