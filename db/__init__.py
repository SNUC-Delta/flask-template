from .setup import init_db

init_db()

from .models import User
from .db import get_threadspecific_cursor