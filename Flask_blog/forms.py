from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanForm
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistrationForm(FlaskForm):
	username=StringField("Username", validators=[DataRequired(),Length(min=5,max=12)])
	email=StringField('Email', validators=[DataRequired(),Email()])
	password=PasswordField("Password", validators=[DataRequired(),Length(min=6, max=15)])
	confirm_password=PasswordField("Confirm Password", 
				validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField("Sign Up")




class LoginForm(FlaskForm):
	
	email=StringField('Email', validators=[DataRequired(),Email()])
	password=PasswordField("Password", validators=[DataRequired(),Length(min=6, max=15)])
	remember=BooleanForm('Remember Me')
	submit=SubmitField("Login")
