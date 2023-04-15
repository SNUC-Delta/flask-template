from flask import Flask

app = Flask(__name__)

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET = os.environ.get("FLASK_SECRET")
if not SECRET:
    from secrets import token_hex
    SECRET = token_hex(16)

app.config['SECRET_KEY'] = SECRET