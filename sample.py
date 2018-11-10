from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config/config.py')

db = MySQL(app)

from view.app_view import *

if __name__ == '__main__':
    app.run(debug=True)