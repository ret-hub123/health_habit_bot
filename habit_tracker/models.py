from flask_login import UserMixin

from .build_model import db, login_manager
from .constant import IconEnum, UnitEnum, FrequencyEnum, DayEnum
from datetime import datetime, timezone, date


class Habit(db.Model):
    """Модель привычки"""
    __tablename__ = 'habits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    icon = db.Column(db.String(50), default='pin', nullable=False)
    color = db.Column(db.String(7), default='#2ea44f')
    target = db.Column(db.Integer)
    unit = db.Column(db.String(50), nullable=True)
    frequency = db.Column(db.String(50), default='daily', nullable=False)

    reminder_time = db.Column(db.Time)
    reminder_days = db.Column(db.String(50))

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    logs = db.relationship('HabitLog', backref='habit', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Habit {self.name}, owner - > {self.user_id.username}'

    def is_completed_today(self):
        today = date.today()
        for log in self.logs:
            if log.date == today:
                return log.completed
        return False

    def get_icon_emoji(self):
        return IconEnum.get_emoji(self.icon)

    def get_unit_label(self):
        return UnitEnum.get_label(self.unit) if self.unit else ''

    def get_frequency_label(self):
        return FrequencyEnum.get_label(self.frequency)


class HabitLog(db.Model):
    """Лог выполнения привычки"""
    __tablename__ = 'habit_logs'

    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=lambda: date.today())
    completed = db.Column(db.Boolean, default=True)

    value = db.Column(db.Integer, nullable=True)
    note = db.Column(db.String(200), nullable=True)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<HabitLog {self.habit.name} - {self.date}>'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """Модель пользователи"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

    habits = db.relationship('Habit', backref = 'user', lazy = True)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
