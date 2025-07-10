from flask import Flask
from portal.config import configure


def create_app():
    app = Flask(__name__)
    configure(app)
    return app

if __name__ == '__main__':
    create_app().run()