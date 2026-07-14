from .build_model import db
from .constant import IconEnum, UnitEnum, FrequencyEnum, DayEnum
from datetime import datetime, timezone

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

    # Напоминание
    reminder_time = db.Column(db.Time)
    reminder_days = db.Column(db.String(50))

    # Системные поля
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Habit {self.name}, owner - >'

    def get_icon_emoji(self):
        return IconEnum.get_emoji(self.icon)

    def get_unit_label(self):
        return UnitEnum.get_label(self.unit) if self.unit else ''

    def get_frequency_label(self):
        return FrequencyEnum.get_label(self.frequency)