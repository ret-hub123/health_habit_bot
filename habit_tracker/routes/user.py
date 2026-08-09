from flask import Blueprint, redirect, url_for, flash, request
from flask import render_template
from flask_login import login_user, logout_user, current_user, login_required

from ..forms import RegistrationFrom, LoginFrom
from ..models import User
from ..build_model import db, bcrypt


user = Blueprint('user', __name__)

@user.route('/user_account')
def user_account():
    return render_template('main/user.html')

@user.route('/registration', methods=['GET', 'POST'])
def user_registration():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            login = form.login.data,
            username = form.username.data,
            email = form.email.data,
            password = hashed_password,
        )

        try:
            db.session.add(user)
            db.session.commit()
            flash('Регистрация успешна!', 'success')
            return redirect('/main')
        except Exception as e:
            db.session.rollback()
            print(e)
            flash('Произошла ошибка при регистрации. Попробуйте еще раз.', 'danger')


    return render_template('main/registration.html', form = form)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Вы уже авторизованы!', 'info')
        return redirect(url_for('habit.main_page'))
    form = LoginFrom()

    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Успешная авторизация пользователя {user.username}', 'success')
            return redirect(next_page) if next_page else redirect('/main')
        else:
            flash(f'Ошибка входа, пожалуйста проверьте свой логин и пароль', "warning")

    return render_template('main/authorization.html', form = form)

@user.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли из системы', 'info')
    return redirect('/main')