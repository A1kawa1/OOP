from rest_framework.exceptions import APIException

class NoToken(APIException):
    status_code = 401
    default_detail = 'Token must be present'


class InvalideToken(APIException):
    status_code = 401
    default_detail = 'Token is invalid'
