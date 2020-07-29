# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user

from . import web

from app.forms.auth import RegisterForm, LoginForm, EmailForm
from app.models.user import User
from app.models.base import db
from app.libs.email import send_mail


@web.route('/register', methods=['GET', 'POST'])
def register():
    """
    注册：1 表单验证+POST
         2 提交用户信息
    :return:
    """
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            user.password = form.password.data
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或者密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    """
    忘记密码: 发起忘记密码请求,发送邮件
    :return:
    """
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            send_mail(form.email.data, '重置您的密码', 'email/reset_password.html', user=user, token=user.generate_token())
            flash('一封邮件已经发送到邮箱' + account_email + ',请及时查收!')

    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web_index'))
