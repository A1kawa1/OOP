from rest_framework import permissions
from random import choice
from datetime import datetime
import jwt

from api.exceptions import InvalidToken


def authenticate_user(username, password):
    return choice([True, False])


class ProtectedResourcePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Autharization')
        if token is None:
            raise InvalidToken

        try:
            data = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(data)
            if not all(list(map(lambda el: el in data, ['username', 'password', 'start_date']))):
                raise InvalidToken

            if (datetime.strptime(data.get('start_date'), '%Y-%m-%d') - datetime.now()).days > 30:
                raise InvalidToken

            return True
        except Exception as e:
            print(e)
            raise InvalidToken
