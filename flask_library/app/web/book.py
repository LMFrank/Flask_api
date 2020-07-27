# -*- coding: utf-8 -*-
import json

from flask import request, render_template, flash
from flask_login import current_user

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
from app.models.gift import Gift
from app.models.wish import Wish


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

    return render_template('search_result.html',
                           books=books,
                           form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
    书籍详情页展示：1 包含书籍的相关信息
                 2 所有请求书籍人信息列表
                 3 所有赠送者信息列表
    :param isbn:
    :return:
    """
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html',
                           book=book,
                           gifts=trade_gifts_model,
                           wishes=trade_wishes_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)