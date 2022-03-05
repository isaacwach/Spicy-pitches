from flask import render_template, redirect, request
from . import main 

@main.route('')
def index():

    return render_template('index.html')