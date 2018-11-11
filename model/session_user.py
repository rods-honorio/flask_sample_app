from sqlalchemy import Column, String
from config.database import Base

class SessionUser(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(20), unique=True)

    def __init__(self, username=None, name=None, password=None):
        self.username = username
        self.name = name
        self.password = password

    def __repr__(self):
        return '<SessionUser %r>' % (self.name)
