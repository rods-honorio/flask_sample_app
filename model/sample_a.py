
class SampleA:
    def __init__(self, text_field_a, numeric_field_a, date_field_a, id_field_a=None):
        self.__id_field_a  = id_field_a
        self.__text_field_a = text_field_a
        self.__numeric_field_a = numeric_field_a
        self.__date_field_a = date_field_a

    @property
    def id_field_a(self):
        return self.__id_field_a

    @id_field_a.setter
    def id_field_a(self, id_field_a):
        self.__id_field_a = id_field_a

    @property
    def text_field_a(self):
        return self.__text_field_a

    @text_field_a.setter
    def text_field_a(self, text_field_a):
        self.__text_field_a = text_field_a

    @property
    def numeric_field_a(self):
        return self.__numeric_field_a

    @numeric_field_a.setter
    def numeric_field_a(self, numeric_field_a):
        self.__numeric_field_a = numeric_field_a

    @property
    def date_field_a(self):
        return self.__date_field_a

    @date_field_a.setter
    def date_field_a(self, date_field_a):
        self.__date_field_a = date_field_a

