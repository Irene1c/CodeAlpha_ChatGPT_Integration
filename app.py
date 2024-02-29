"""Running flask app"""

from chatapp import create_app, socketio

app = create_app()


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
