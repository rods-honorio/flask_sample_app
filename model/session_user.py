from dao import db


class SessionUser(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20), unique=True)

    def __init__(self, username=None, name=None, password=None):
        self.username = username
        self.name = name
        self.password = password

    def __repr__(self):
        return '<SessionUser %r>' % self.name
