# -*- coding: utf-8 -*-
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum


api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generator_auth_token(identity['uid'], form.type.data, None, expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generator_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        # 'scope': scope
    })