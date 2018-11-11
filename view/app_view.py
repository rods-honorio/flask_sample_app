from flask import render_template, send_from_directory
from sample import app
from dao.sample_a_dao import SampleADao
from view import sample_a_view

sample_a_dao = SampleADao()


@app.route('/')
def index():
    sample_list = sample_a_dao.list_sample_a()
    return render_template('list_samples.html', title='Samples', samples=sample_list)


@app.route('/uploads/<file_name>')
def image(file_name):
    return send_from_directory('uploads', file_name)
