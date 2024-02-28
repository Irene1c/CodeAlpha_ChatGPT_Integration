""" Flask app """
from flask import Flask
from dotenv import load_dotenv


def create_app():
    """application factory"""

    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # load configuration settings
    app.config.from_object('config.ConfigClass')

    from chatapp.routes import views
    from chatapp.chatbot import chat

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(chat, url_prefix='/')

    return app
