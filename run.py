from server import app
import os

ENVIRONMENT = os.environ.get("FLASK_ENVIRONMENT", "development")
HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
PORT = os.environ.get("FLASK_PORT", 5000)

if __name__ == '__main__':
    app.run(debug = ENVIRONMENT=="development", host = HOST, port = PORT)