# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from flask_login import current_user

from . import web
from app.models.base import db
from app.models.wish import Wish
from app.view_models.wish import MyWishes


@web.route('/my/wish')
def my_wish():
    """
    心愿清单：保存当前用户数据
            1 用户id
            2 心愿清单列表
            3 礼物
    :return:
    """
    uid = current_user.id
    wish_of_mine = Wish.get_user_wish(uid)
    isbn_list = [wish.isbn for wish in wish_of_mine]
    gift_count_list = Wish.get_gift_count(isbn_list)
    view_model = MyWishes(wish_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.wishes)


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    """
    保存到心愿清单：1 确定是否能保存到清单
                 2 礼物的isbn  用户id
    :param isbn:
    :return:
    """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('该书已经添加至您的赠送清单或已经存在你的心愿清单,请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
