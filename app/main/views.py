from flask import render_template, redirect, request, url_for
from . import main 

@main.route('/')
def index():

    return "Welcome"
