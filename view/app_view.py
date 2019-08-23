from flask import render_template, send_from_directory, Blueprint
from dao import SampleADao

sample_a_dao = SampleADao()

sample_app_bp = Blueprint('sample_app', __name__)


@sample_app_bp.route('/')
def index():
    sample_list = sample_a_dao.list_sample_a()
    return render_template('list_samples.html', title='Samples', samples=sample_list)


@sample_app_bp.route('/uploads/<file_name>')
def image(file_name):
    return send_from_directory('uploads', file_name)
