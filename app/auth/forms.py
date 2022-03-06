from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username = StringField('Enter Your Username', validators=[Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')