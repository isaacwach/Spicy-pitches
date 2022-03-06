import os

class Config:

    SQLALCHEMY_DARABASE_URI=os.environ.get('DATABASE_URL')
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