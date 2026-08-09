from flask import Blueprint

from flask import render_template, request, flash, redirect, url_for
from ..constant import IconEnum, UnitEnum, FrequencyEnum, DayEnum
from ..build_model import db
from ..models import Habit
from flask_login import current_user, login_required

habit = Blueprint('habit', __name__)

@habit.route('/')
@habit.route('/main')
def main_page():
    if current_user.is_authenticated: habbit = Habit.query.filter_by(user_id=current_user.id).all()
    else: habbit = []
    return render_template("main/main.html", habbit=habbit)




@habit.route('/add_habbit', methods=['GET', 'POST'])
@login_required
def add_habbit():
    if request.method == 'POST':
        if not request.form.get('name'):
            flash('Название обязательно!', 'danger')
            return render_template('add habbit.html',
                                   IconEnum=IconEnum,
                                   UnitEnum=UnitEnum,
                                   FrequencyEnum=FrequencyEnum)

        name = request.form['name']
        description = request.form.get('description', '')
        icon = request.form.get('icon', IconEnum.PIN.value)
        color = request.form.get('color', '#2ea44f')
        target_str = request.form.get('target')
        target = int(target_str) if target_str else None
        unit = request.form.get('unit') or None
        frequency = request.form.get('frequency', FrequencyEnum.DAILY.value)
        reminder_time = request.form.get('reminder_time') or None
        reminder_days = request.form.get('reminder_days') or None
        is_active = True if request.form.get('is_active') else False

        habit = Habit(
            name=name,
            description=description,
            icon=icon,
            color=color,
            target=target,
            unit=unit,
            frequency=frequency,
            reminder_time=reminder_time,
            reminder_days=reminder_days,
            is_active=is_active,
            user_id= current_user.id)

        try:
            db.session.add(habit)
            db.session.commit()
            flash('Привычка успешно создана!', 'success')
            return redirect('/main')
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при добавлении привычки', 'danger')
            print(e)
            return render_template('main/add habbit.html',
                                   IconEnum=IconEnum,
                                   UnitEnum=UnitEnum,
                                   FrequencyEnum=FrequencyEnum)

    return render_template('main/add habbit.html',
                           IconEnum=IconEnum,
                           UnitEnum=UnitEnum,
                           FrequencyEnum=FrequencyEnum)



@habit.route('/habit/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_habbit(id):
    habit = Habit.query.get_or_404(id)

    if habit.user_id != current_user.id:
        flash('Доступ запрещён', 'danger')
        return redirect(url_for('habit.main_page'))

    if request.method == 'POST':
        habit.name = request.form['name']
        habit.description = request.form.get('description', '')
        habit.icon = request.form.get('icon', IconEnum.PIN.value)
        habit.color = request.form.get('color', '#2ea44f')
        target_str = request.form.get('target')
        habit.target = int(target_str) if target_str else None
        habit.unit = request.form.get('unit') or None
        habit.frequency = request.form.get('frequency', FrequencyEnum.DAILY.value)
        habit.reminder_time = request.form.get('reminder_time') or None
        habit.reminder_days = request.form.get('reminder_days') or None
        habit.is_active = True if request.form.get('is_active') else False

        try:
            db.session.commit()
            flash('Привычка успешно обновлена!', 'success')
            return redirect(url_for('habit.main_page'))
        except Exception as e:
            db.session.rollback()
            flash('Ошибка при обновлении привычки', 'danger')
            print(e)

    return render_template('main/post_update.html',
                           habit=habit,
                           IconEnum=IconEnum,
                           UnitEnum=UnitEnum,
                           FrequencyEnum=FrequencyEnum)

@habit.route('/habit/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_habbit(id):
    habit = Habit.query.get_or_404(id)

    if habit.user_id != current_user.id:
        flash('Доступ запрещён', 'danger')
        return redirect(url_for('habit.main_page'))

    try:
        db.session.delete(habit)
        db.session.commit()
        flash('Привычка успешно удалена!', 'success')

    except Exception as e:
        db.session.rollback()
        flash('Ошибка при удалении привычки', 'danger')
        print(e)

    return redirect(url_for('habit.main_page'))