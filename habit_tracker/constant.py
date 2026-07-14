import enum

class MainEnum(enum.Enum):

    @classmethod
    def choices(cls):
        """Возвращает список для выпадающего списка: [(value, label), ...]"""
        return [(item.value, item.name) for item in cls]

    @classmethod
    def get_by_value(cls, value):
        """Возвращает значение value"""
        for item in cls:
            if item.value == value:
                return item
        return None


class IconEnum(MainEnum):

    WATER = 'water'
    RUN = 'run'
    READ = 'read'
    MEDITATE = 'meditate'
    EAT = 'eat'
    SPORT = 'sport'
    TARGET = 'target'
    STAR = 'star'
    FIRE = 'fire'
    PIN = 'pin'
    ART = 'art'
    SLEEP = 'sleep'
    BRAIN = 'brain'
    HEALTH = 'health'
    MORNING = 'morning'
    MUSIC = 'music'
    WRITE = 'write'
    TALK = 'talk'
    WORK = 'work'
    HOME = 'home'
    NATURE = 'nature'
    OCEAN = 'ocean'

    @classmethod
    def get_emoji(cls, value):
        emoji_map = {
            'water': '💧',
            'run': '🏃',
            'read': '📖',
            'meditate': '🧘',
            'eat': '🥗',
            'sport': '💪',
            'target': '🎯',
            'star': '⭐',
            'fire': '🔥',
            'pin': '📌',
            'art': '🎨',
            'sleep': '💤',
            'brain': '🧠',
            'health': '❤️',
            'morning': '🌅',
            'music': '🎵',
            'write': '✍️',
            'talk': '🗣️',
            'work': '💼',
            'home': '🏠',
            'nature': '🌿',
            'ocean': '🌊'
        }
        return emoji_map.get(value, '📌')


class UnitEnum(MainEnum):
    TIMES = 'разы'
    LITERS = 'литра'
    MINUTES = 'минуты'
    HOURS = 'часы'
    PAGES = 'страницы'
    KM = 'км'
    STEPS = 'шаги'
    CALORIES = 'калории'
    GRAMS = 'граммы'
    LAPS = 'круги'
    SETS = 'подходы'
    GLASSES = 'стаканы'

    @classmethod
    def get_label(cls, value):
        labels = {
            'разы': 'раз(а)',
            'литра': 'литр(ов)',
            'минуты': 'минут(ы)',
            'часы': 'час(ов)',
            'страницы': 'страниц(ы)',
            'км': 'км',
            'шаги': 'шаг(ов)',
            'калории': 'калорий(и)',
            'граммы': 'грамм(ов)',
            'круги': 'круг(ов)',
            'подходы': 'подход(ов)',
            'стаканы': 'стакан(ов)'
        }
        return labels.get(value, value)


class FrequencyEnum(MainEnum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

    @classmethod
    def get_label(cls, value):
        labels = {
            'daily': 'Ежедневно',
            'weekly': 'Еженедельно',
            'monthly': 'Ежемесячно'
        }
        return labels.get(value, value)


class DayEnum(MainEnum):
    MON = 'mon'
    TUE = 'tue'
    WED = 'wed'
    THU = 'thu'
    FRI = 'fri'
    SAT = 'sat'
    SUN = 'sun'