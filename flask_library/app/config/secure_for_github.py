# -*- coding: utf-8 -*-
DEBUG = True

# 单数据库
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://user:password@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'SECRET_KEY'

# Email相关配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'xxx.@163.com'
MAIL_PASSWORD = 'xxx'
