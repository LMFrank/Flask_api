# -*- coding: utf-8 -*-
from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_mail(to, subject, template, **kwargs):
    msg = Message('[鱼书]' + '' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg = render_template(template, **kwargs)
    mail.send(msg)

