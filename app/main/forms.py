from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProfileUpdate(FlaskForm):
    profile_bio=TextAreaField('Tell us about yourself.', validators=[DataRequired()])
    submit=StringField('Save')

class PitchForm(FlaskForm):
    title=TextField('Title', validators=[DataRequired()])
    category=TextField('Category', categories=[('Motivation', 'Motivation'), ('Jokes', 'Jokes'), ('Education', 'Education')], validators=[DataRequired()])
    post= TextAreaField('Enter pitch', validators=[DataRequired()])