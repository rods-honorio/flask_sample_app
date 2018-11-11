from flask import Flask
from config.database import db_session, init_db

app = Flask(__name__)
app.config.from_pyfile('config/config.py')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()

from view.app_view import *

if __name__ == '__main__':
    app.run(debug=True)