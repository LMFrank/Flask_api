# -*- coding: utf-8 -*-
from app.models.base import Base, db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, func, desc
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)