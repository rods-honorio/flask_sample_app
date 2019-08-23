from flask import render_template, Blueprint
from dao.database import db

errors_bp = Blueprint('errors', __name__)


@errors_bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='404 Error D:'), 404


@errors_bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html', title='500 Error D:'), 500
