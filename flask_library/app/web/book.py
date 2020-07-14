# -*- coding: utf-8 -*-
from flask import request, jsonify

from app.libs.helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm


@web.route('/book/search/')
def search():
    """
    搜索
    q:[普通关键字 isbn]
    page：页码
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.q.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
