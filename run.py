from flask import Flask
from app import api_bp


def create_app(config_filename):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_filename)
    flask_app.register_blueprint(api_bp, url_prefix='/api')
    return flask_app


if __name__ == "__main__":
    app = create_app("config")
    app.run()
