from flask import render_template
from . import main 

@app.route('/')
def index():

    return render_template('index.html')