from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    Registration form for new users
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Fsername', validators=[DataRequired()])
    first_name = StringField('Firstname', validators=[DataRequired()])
    last_name = StringField('Lastname', validators=[DataRequired()])
    password = PasswordField('Password', valdators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField("Register")

    def validate_email(self, field):
        """
        Ensure unique emails
        """
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError("An account with the email you provided exists.")


    def validate_username(self, field):
        """
        Ensure unique usernames
        """
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError("An account with the username you provided exists.")


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')