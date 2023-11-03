from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class EventForm(FlaskForm):
    name=StringField('Name')
    description=TextAreaField('Description')
    image = StringField('Image File Name')
    submit = SubmitField("Create")

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    contact_number = StringField('Contact Number')
    address = StringField('Address')

class ContactForm(FlaskForm):
    user_name = StringField('Name' )    
    email = StringField('Email Address')
    submit = SubmitField("Submit")

    #submit button
    submit = SubmitField("Register")