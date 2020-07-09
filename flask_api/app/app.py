# -*- coding: utf-8 -*-
from flask import Flask


def register_blueprints(app):
    from app.api.v1 import create_bluprint_v1
    app.register_blueprint(create_bluprint_v1(), url_prefix='/v1')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    return app


