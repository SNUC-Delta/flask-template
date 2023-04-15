from .app import app
from .auth import auth


app.register_blueprint(auth, url_prefix='/auth')