from model import SessionUser


class SessionUserDao:

    def search_by_id(self, username):
        return SessionUser.query.filter(SessionUser.username == username).first()


def create_user(tupla):
    return SessionUser(tupla[0], tupla[1], tupla[2])