from flask import render_template, redirect, request
from . import main 

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/user/<name>')
def profiles(name):

    return render_template('profile.html')