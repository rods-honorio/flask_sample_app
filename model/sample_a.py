from dao import db


class SampleA(db.Model):
    __tablename__ = 'sample_a'
    id_field_a = db.Column(db.Integer, primary_key=True)
    text_field_a = db.Column(db.String(50), unique=True)
    numeric_field_a = db.Column(db.Integer, unique=True)
    date_field_a = db.Column(db.Date, unique=True)

    def __init__(self, text_field_a=None, numeric_field_a=None, date_field_a=None, id_field_a=None):
        self.id_field_a = id_field_a
        self.text_field_a = text_field_a
        self.numeric_field_a = numeric_field_a
        self.date_field_a = date_field_a

    def __repr__(self):
        return '<SampleA %r>' % self.id_field_a


