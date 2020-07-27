# -*- coding: utf-8 -*-
from . import web


@web.route('/')
def index():
    pass


@web.route('/personal')
def personal_center():
    pass
