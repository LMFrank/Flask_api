# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from app.models.base import db


login_manager = LoginManager()


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
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
