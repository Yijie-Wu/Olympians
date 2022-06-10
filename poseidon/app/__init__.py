import os

import click
from flask import Flask, jsonify
from flask_wtf.csrf import CSRFError

from .settings import config
from app.apis.v1 import api_v1


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('app')

    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(api_v1, url_prefix='/api/v1')

def register_commands(app):
    pass
