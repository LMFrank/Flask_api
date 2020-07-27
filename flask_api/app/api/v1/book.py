# -*- coding: utf-8 -*-
from app.libs.redprint import Redprint


api = Redprint('book')


@api.route('/get')
def get_book():
    return "get book"


@api.route('/create')
def create_book():
    return 'create book'