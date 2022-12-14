from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import EmailField, TelField


class LoginForm(FlaskForm):
    name = StringField('Name:', id='name')
    phone = TelField('Phone Number:', id='name')
    email = EmailField('Email:', id='mail')
    job = StringField('Job Title:', id='name')
