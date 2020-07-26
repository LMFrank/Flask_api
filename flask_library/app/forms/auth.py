# -*- coding: utf-8 -*-
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length,DataRequired,Email, ValidationError,EqualTo

from app.models.user import User


class RegisterForm(Form):
    """表单验证"""
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空')])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符,最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经存在')