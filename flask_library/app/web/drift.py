# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from . import web
from app.models.gift import Gift


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    """
    向他人请求此书：1 判断能否请求
                 2 判断书籍的id 与 归属
                 3 请求的详情页面
                 4 发送邮件申请
    :param gid:
    :return:
    """
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_your_gift(current_user.id):
        flash('这本书属于你,不能向自己所要哦!!')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))

    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)

    gifter = current_gift.user.summary

    return render_template('drift.html', gifter=gifter, user_beans=current_user.beans)


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
