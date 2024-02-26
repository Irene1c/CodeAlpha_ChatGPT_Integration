""" Flask app """

from flask import Flask

def create_app():
    """application factory"""

    app = Flask(__name__)

    # load configuration settings
    app.config.from_object('config.ConfigClass')

    from chatapp.routes import views

    app.register_blueprint(views, url_prefix='/')

    return app
