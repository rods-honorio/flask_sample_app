from model.session_user import SessionUser

SQL_USUARIO_POR_ID = 'SELECT username, name, password from users where username = %s'

class SessionUserDao:
    def __init__(self, db):
        self.__db = db

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        sample_data = cursor.fetchone()
        session_user = create_user(sample_data) if sample_data else None
        return session_user

def create_user(tupla):
    return SessionUser(tupla[0], tupla[1], tupla[2])