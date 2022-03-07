import os
from dotenv import load_dotenv
load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY=os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass 

class ProdConfig(Config):
    pass  

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'Production':ProdConfig
}