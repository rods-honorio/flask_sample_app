from flask import render_template, Blueprint
from dao.database import db
from flask import current_app

errors_bp = Blueprint('errors', __name__)


@errors_bp.errorhandler(404)
def not_found_error(error):
    current_app.logger.error(error)
    return render_template('404.html', title='404 Error D:'), 404


@errors_bp.errorhandler(500)
def internal_error(error):
    current_app.logger.error(error)
    db.session.rollback()
    return render_template('500.html', title='500 Error D:'), 500
