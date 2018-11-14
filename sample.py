from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from dao.database import db
    db.init_app(app)

    from view.app_view import sample_app_bp
    from view.sample_a_view import sample_a_bp
    from view.session_view import session_bp
    app.register_blueprint(sample_app_bp)
    app.register_blueprint(sample_a_bp)
    app.register_blueprint(session_bp)

    return app

if __name__ == '__main__':
    create_app('config/config.py').run(debug=True)