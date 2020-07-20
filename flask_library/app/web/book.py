# -*- coding: utf-8 -*-
import json

from flask import request, render_template, flash

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection


@web.route('/book/search/')
def search():
    """
    搜索
    q:[普通关键字 isbn]
    page：页码
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('您输入的搜索关键字不符合要求,请重新输入')

    return render_template('search_result.html', books=books, form=form)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass