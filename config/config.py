import os

SECRET_KEY = 'rods'
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "M4n43lf0v41!"
MYSQL_DB = "sample"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath('sample.py')) + '/uploads'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:M4n43lf0v41!@localhost/sample'
SQLALCHEMY_TRACK_MODIFICATIONS = False