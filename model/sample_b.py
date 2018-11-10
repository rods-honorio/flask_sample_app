
class SampleB:
    def __init__(self, text_field_b, id_field_a, id_field_b=None):
        self.__id_field_b = id_field_b
        self.__id_field_a  = id_field_a
        self.__text_field_b = text_field_b

    @property
    def id_field_a(self):
        return self.__id_field_a

    @id_field_a.setter
    def id_field_a(self, id_field_a):
        self.__id_field_a = id_field_a

    @property
    def id_field_b(self):
        return self.__id_field_b

    @id_field_b.setter
    def id_field_b(self, id_field_b):
        self.__id_field_b = id_field_b

    @property
    def text_field_b(self):
        return self.__text_field_a

    @text_field_b.setter
    def text_field_a(self, text_field_b):
        self.__text_field_b = text_field_b
