from flask import Flask
from config import DevConfig

def create_app(config_name):
    app= Flask(__name__)

    return app 