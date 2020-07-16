# -*- coding: utf-8 -*-
from flask import current_app
from app.libs.httper import Http


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calulate_start(page))
        result = Http.get(url)
        return result

    @staticmethod
    def calulate_start(page):
        return (page - 1) * current_app.config.get('PER_PAGE')
