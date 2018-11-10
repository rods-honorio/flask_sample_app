from model.sample_a import SampleA

SQL_DELETA_SAMPLE_A = 'delete from sample_a where id_field_a = %s'
SQL_SAMPLE_A_POR_ID = 'SELECT id_field_a, text_field_a, numeric_field_a, date_field_a from sample_a ' \
                      'where id_field_a = %s '
SQL_ATUALIZA_SAMPLE_A = 'UPDATE sample_a SET id_field_a=%d, text_field_a=%s, numeric_field_a=%d, date_field_a=%s, ' \
                        'where id_field_a = %s'
SQL_BUSCA_SAMPLE_A = 'SELECT id_field_a, text_field_a, numeric_field_a, date_field_a from sample_a'
SQL_CRIA_SAMPLE_A = 'INSERT into sample_a (text_field_a, numeric_field_a, date_field_a) values (%s, %s, %s)'


class SampleADao:
    def __init__(self, db):
        self.__db = db

    def save_sample_a(self, sample_a):
        cursor = self.__db.connection.cursor()

        if sample_a.id_field_a:
            cursor.execute(SQL_ATUALIZA_SAMPLE_A, (sample_a.text_field_a, sample_a.numeric_field_a,
                                                   sample_a.date_field_a,
                                                   sample_a.id_field_a))
        else:
            cursor.execute(SQL_CRIA_SAMPLE_A, (sample_a.text_field_a, sample_a.numeric_field_a,
                                               sample_a.date_field_a))

            sample_a.id_field_a = cursor.lastrowid
        self.__db.connection.commit()
        return sample_a

    def list_sample_a(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SAMPLE_A)
        sample_a_list = create_sample_a_list(cursor.fetchall())
        return sample_a_list

    def search_by_id_sample_a(self, id_field_a):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SAMPLE_A_POR_ID, (id_field_a,))
        sample_a_tuple = cursor.fetchone()
        return SampleA(sample_a_tuple[1], sample_a_tuple[2], sample_a_tuple[3], id_field_a=sample_a_tuple[0])

    def delete_sample_a(self, id_field_a):
        self.__db.connection.cursor().execute(SQL_DELETA_SAMPLE_A, (id_field_a,))
        self.__db.connection.commit()


def create_sample_a_list(sample_a_list):
    def create_sample_a(sample_a_tuple):
        return SampleA(sample_a_tuple[1], sample_a_tuple[2], sample_a_tuple[3], id_field_a=sample_a_tuple[0])
    return list(map(create_sample_a, sample_a_list))
