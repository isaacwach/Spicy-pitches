from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    subject_pref = 'Tweet it!'
    sender_email = 'spicypitch@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.html = render_template(template + ".html",**kwargs)
    email.body= render_template(template + ".txt",**kwargs)
    mail.send(email)