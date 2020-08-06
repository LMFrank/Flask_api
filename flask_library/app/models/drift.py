# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base


class Drift(Base):
    """鱼漂：一次具体的交易的信息"""

    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)  # 收件人姓名
    address = Column(String(100), nullable=False)
    message = Column(String(200))  # 留言
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    # 鱼漂的状态
    _pending = Column('pending', SmallInteger, default=1)