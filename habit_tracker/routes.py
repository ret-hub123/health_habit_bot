from flask import Blueprint

from flask import render_template, request, flash, redirect, url_for
from .constant import IconEnum, UnitEnum, FrequencyEnum, DayEnum
from .build_model import db
from .models import Habit

habit = Blueprint('habit', __name__)

@habit.route('/')
@habit.route('/main')
def main_page():
    habbit = Habit.query.all()
    return render_template("main.html", habbit=habbit)


@habit.route('/add_habbit', methods=['GET', 'POST'])
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
            is_active=is_active)

        try:
            db.session.add(habit)
            db.session.commit()
            flash('Привычка успешно создана!', 'success')
            return redirect('/main')
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при добавлении привычки: {str(e)}', 'danger')
            return render_template('add habbit.html',
                                   IconEnum=IconEnum,
                                   UnitEnum=UnitEnum,
                                   FrequencyEnum=FrequencyEnum)

    return render_template('add habbit.html',
                           IconEnum=IconEnum,
                           UnitEnum=UnitEnum,
                           FrequencyEnum=FrequencyEnum)
