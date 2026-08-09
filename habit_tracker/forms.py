
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from .models import User


class RegistrationFrom(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    username = StringField('Имя пользователя')
    email = StringField('Email')
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль',
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login = login.data).first()
        if user: raise ValidationError(f"Данное имя: {login.data} уже занято, выберите другое")

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user: raise ValidationError(f"Данная почта: {email.data} уже зарегистрирована на другом аккаунте")


class LoginFrom(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')