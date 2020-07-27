# -*- coding: utf-8 -*-
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'OK'
    error_code = 0


class ServerError(APIException):
    code = 500
    error_code = 999
    msg = 'sorry, we make a mistake'


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
    description = (
        'client is invalid'
    )


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1002