class SessionUser:
    def __init__(self, username, name, password):
        self.__username = username
        self.__name = name
        self.__password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password