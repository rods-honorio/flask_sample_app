from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/config.py')

    from dao.database import db
    db.init_app(app)

    from view.app_view import sample_app_bp
    from view.sample_a_view import sample_a_bp
    from view.session_view import session_bp
    from view.error_view import errors_bp, not_found_error
    app.register_blueprint(sample_app_bp, url_prefix='/flask')
    app.register_blueprint(sample_a_bp, url_prefix='/flask')
    app.register_blueprint(session_bp, url_prefix='/flask')
    app.register_blueprint(errors_bp, url_prefix='/flask')
    app.register_error_handler(404, not_found_error)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
