import os

class Config:

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + pitches
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #SECRET_KEY=os.environ.get('SECRET_KEY')
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