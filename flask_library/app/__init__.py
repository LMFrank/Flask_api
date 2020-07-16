# -*- coding: utf-8 -*-
from flask import Flask
from app.models.book import db


def create_app():
    """
    系统配置与蓝图需要绑定app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
