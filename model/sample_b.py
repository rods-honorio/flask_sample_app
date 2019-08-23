from dao import db


class SampleB(db.Model):
    __tablename__ = 'sample_b'
    id_field_b = db.Column(db.Integer, primary_key=True)
    id_field_a = db.Column(db.Integer, primary_key=True)
    text_field_b = db.Column(db.String(50), unique=True)

    def __init__(self, text_field_b=None, id_field_b=None, id_field_a=None):
        self.id_field_b = id_field_b
        self.id_field_a = id_field_a
        self.text_field_b = text_field_b

    def __repr__(self):
        return '<SampleB %r>' % self.id_field_b + ' - ' + self.id_field_a
