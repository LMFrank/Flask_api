# -*- coding: utf-8 -*-


class AdminScope(object):
    allow_api = ['v1.super_get_user']


class UserScope(object):
    allow_api = []


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False


