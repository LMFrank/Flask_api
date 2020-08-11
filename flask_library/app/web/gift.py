# -*- coding: utf-8 -*-
from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from . import web
from app.models.gift import Gift
from app.models.base import db
from app.view_models.gift import MyGifts
from app.libs.enums import PendingStatus
from app.models.drift import Drift


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经添加至您的赠送清单或已存在您的心愿清单,不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    """
    赠送清单中撤销操作：1 查询所有礼物 鱼漂
                    2 礼物状态修改  鱼漂数值撤销
    :param gid:
    :return:
    """
    gift = Gift.query.filter_by(id=gid, launched=False).first()
    if not gift:
        flash('该书籍不存在,或已经处于交易状态,撤销失败!')
    drift = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.Waiting).first()
    if drift:
        flash('这个礼物正处于交易状态,请先在鱼漂处完成交易!')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))



