from api.models import Token
from rest_framework import permissions

from api.exceptions import NoToken, InvalideToken


class TokenPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.query_params.get('token')
        print(token)
        if token is None:
            raise NoToken

        try:
            token_exist = Token.objects.filter(token=token).exists()
            if not token_exist:
                raise InvalideToken
        except:
            raise InvalideToken

        return True