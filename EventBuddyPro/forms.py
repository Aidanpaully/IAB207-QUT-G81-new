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
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

class ContactForm(FlaskForm):
    user_name = StringField('Name' )    
    email = StringField('Email Address')
    submit = SubmitField("Submit")

    #submit button
    submit = SubmitField("Register")