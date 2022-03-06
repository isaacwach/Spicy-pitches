import os

class Config:

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + pitches
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'
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