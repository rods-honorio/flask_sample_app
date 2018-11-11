from sqlalchemy import Column, Integer, String, Date
from config.database import Base


class SampleA(Base):
    __tablename__ = 'sample_a'
    id_field_a = Column(Integer, primary_key=True)
    text_field_a = Column(String(50), unique=True)
    numeric_field_a = Column(Integer, unique=True)
    date_field_a = Column(Date, unique=True)

    def __init__(self, text_field_a=None, numeric_field_a=None, date_field_a=None, id_field_a=None):
        self.id_field_a = id_field_a
        self.text_field_a = text_field_a
        self.numeric_field_a = numeric_field_a
        self.date_field_a = date_field_a

    def __repr__(self):
        return '<SampleA %r>' % (self.id_field_a)


