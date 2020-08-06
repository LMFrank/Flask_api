# -*- coding: utf-8 -*-
from enum import Enum


class PendingStatus(Enum):
    """交易状态"""
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4