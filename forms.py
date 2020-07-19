from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    mail = StringField('Ваша почта', [InputRequired()])
    password = StringField('Введите пароль', [InputRequired()])

class RegistForm(FlaskForm):
    name = StringField('Ваше имя', [InputRequired()])
    mail = StringField('Ваша почта', [InputRequired()])
    password = StringField('Введите пароль', [InputRequired()])
    phone = StringField('Введите ваш номер телефона', [InputRequired()])