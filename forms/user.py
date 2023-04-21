from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField, EmailField
#from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

    
class HelpingForm(FlaskForm):
    problem = TextAreaField("Опишите Вашу проблему", validators=[DataRequired()])
    geo = StringField("Ваш адрес", validators=[DataRequired()])
    number = StringField("Ваш номер", validators=[DataRequired()])
    submit = SubmitField('Отправить')
