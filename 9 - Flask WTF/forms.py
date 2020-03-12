from flask_wtf import FlaskForm
from wtforms import PasswordField,TextField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = TextField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])