import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    USER = os.environ.get('POSTGRESQL_USER', )
    PASSWORD = os.environ.get('POSTGRESQL_PASSWORD', )
    HOST = os.environ.get('POSTGRESQL_HOST', 'localhost')
    PORT = os.environ.get('POSTGRESQL_PORT', '5433')
    DB = os.environ.get('POSTGRESQL_DB', 'habit_tracker_db')

    KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI  = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS  = True
    SECRET_KEY = KEY
