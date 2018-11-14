from model import SampleA
from dao import db


class SampleADao:

    def create_sample_a(self, sample_a):
        db.session.add(sample_a)
        db.session.commit()

    def update_sample_a(self, sample_a):
        sample = SampleA.query.get(sample_a.id_field_a)
        sample.text_field_a = sample_a.text_field_a
        sample.numeric_field_a = sample_a.numeric_field_a
        sample.date_field_a = sample_a.date_field_a
        db.session.commit()

    def list_sample_a(self):
        return SampleA.query.all()

    def search_by_id_sample_a(self, id_field_a):
        return SampleA.query.get(id_field_a)

    def delete_sample_a(self, id_field_a):
        sample_a = SampleA.query.get(id_field_a)
        db.session.delete(sample_a)
        db.session.commit()


def create_sample_a_list(sample_a_list):
    def create_sample_a(sample_a_tuple):
        return SampleA(sample_a_tuple[1], sample_a_tuple[2], sample_a_tuple[3], id_field_a=sample_a_tuple[0])

    return list(map(create_sample_a, sample_a_list))
