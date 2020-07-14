# -*- coding: utf-8 -*-
from flask import Blueprint,render_template


web = Blueprint('web',__name__)


@web.app_errorhandler(404)
def not_found(e):
    """
    AOP: 处理所有的404请求
    """
    return render_template('404.html'),404

@web.app_errorhandler(500)
def internal_server_error(e):
    """
    AOP: 处理所有的500请求
    """
    return render_template('500.html'),500


from app.web import book
from app.web import user