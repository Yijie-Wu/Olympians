from flask import Flask

from .settings import Settings


def create_app():
    app = Flask('app')

    app.config.from_object(Settings)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)

    return app


def register_blueprints(app):
    pass


def register_extensions(app):
    pass


def register_commands(app):
    pass


def register_errors(app):
    pass
