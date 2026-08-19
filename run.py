import os
from habit_tracker import create_app

from dotenv import load_dotenv
load_dotenv('.env')

application = create_app()