from flask import render_template, redirect, request, url_for
from . import main 

@main.route('/')
def index():
    pitches = Pitch.query.all()
    motivation = Pitch.query.filter_by(category = 'Motivation').all() 
    jokes = Pitch.query.filter_by(category = 'Jokes').all()
    education = Pitch.query.filter_by(category = 'Education').all()

    return render_template('index.html', pitches=pitches, education=education, motivation=motivation, jokes=jokes)
