import os
from dotenv import load_dotenv
load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
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