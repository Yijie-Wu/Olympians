import os
from dotenv import load_dotenv
from app.settings import BASE_DIR

dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file)

from app import create_app

app = create_app('development')
