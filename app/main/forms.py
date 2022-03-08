from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from ..models import User

class ProfileUpdate(FlaskForm):
    profile_bio=TextAreaField('Tell us about yourself.', validators=[DataRequired()])
    submit=StringField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    title=TextAreaField('Title', validators=[DataRequired()])
    category=TextAreaField('Category', categories=[('Motivation', 'Motivation'), ('Jokes', 'Jokes'), ('Education', 'Education')], validators=[DataRequired()])
    post= TextAreaField('Enter pitch', validators=[DataRequired()])