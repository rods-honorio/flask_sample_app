from model.sample_b import SampleB

SQL_DELETA_SAMPLE_B = 'delete from sample_b where id_field_b = %d'
SQL_SAMPLE_B_POR_ID = 'SELECT id_field_b, id_field_a, text_field_b where id_field_b = %d '
SQL_ATUALIZA_SAMPLE_B = 'UPDATE sample_b SET id_field_a=%d, text_field_b=%s ' \
                        'where id_field_b = %d'
SQL_BUSCA_SAMPLE_B = 'SELECT id_field_b, id_field_a, text_field_b from sample_b'
SQL_CRIA_SAMPLE_B = 'INSERT into sample_b (text_field_b, id_field_a) values (%s, %d)'


class SampleBDao:
    def __init__(self, db):
        self.__db = db

    def save_sample_b(self, sample_b):
        cursor = self.__db.connection.cursor()

        if sample_b.id_field_b:
            cursor.execute(SQL_ATUALIZA_SAMPLE_B, (sample_b.text_field_b, sample_b.id_field_a, sample_b.id_field_b))
        else:
            cursor.execute(SQL_CRIA_SAMPLE_B, (sample_b.text_field_b, sample_b.id_field_a))

            sample_b.id_field_b = cursor.lastrowid
        self.__db.connection.commit()
        return sample_b

    def list_sample_b(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SAMPLE_B)
        sample_b_list = self.create_sample_b_list(cursor.fetchall())
        return sample_b_list

    def search_by_id_sample_b(self, id_field_b):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SAMPLE_B_POR_ID, (id_field_b,))
        sample_b_tuple = cursor.fetchone()
        return SampleB(sample_b_tuple[1], sample_b_tuple[2], id_field_b=sample_b_tuple[0])

    def delete_sample_b(self, id_field_b):
        self.__db.connection.cursor().execute(SQL_DELETA_SAMPLE_B, (id_field_b,))
        self.__db.connection.commit()

    def create_sample_b_list(sample_b_list):
        def create_sample_b(sample_b_tuple):
            return SampleB(sample_b_tuple[1], sample_b_tuple[2], id_field_b=sample_b_tuple[0])

        return list(map(create_sample_b, sample_b_list))
