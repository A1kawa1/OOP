from rest_framework.exceptions import APIException


class InvalidToken(APIException):
    status_code = 403
    default_detail = 'permission denied'


class PostDenied(APIException):
    status_code = 403
    default_detail = 'permission denied'
