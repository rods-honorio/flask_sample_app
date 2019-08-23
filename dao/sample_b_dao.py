from model import SampleB
from dao import db


class SampleBDao:

    def create_sample_b(self, sample_b):
        db.session.add(sample_b)
        db.session.commit()

    def update_sample_b(self, sample_b):
        sample = SampleB.query.get(sample_b.id_field_b, sample_b.id_field_a)
        sample.text_field_b = sample_b.text_field_a
        db.session.commit()

    def list_sample_a(self):
        return SampleB.query.all()

    def search_by_id_sample_a(self, id_field_b, id_field_a):
        return SampleB.query.get(id_field_b, id_field_a)

    def delete_sample_a(self, id_field_b, id_field_a):
        sample_a = SampleB.query.get(id_field_b, id_field_a)
        db.session.delete(sample_a)
        db.session.commit()


def create_sample_a_list(sample_b_list):
    def create_sample_b(sample_a_tuple):
        return SampleB(sample_a_tuple[3],
                       id_field_b=sample_a_tuple[0], id_field_a=sample_a_tuple[1])

    return list(map(create_sample_b, sample_b_list))

