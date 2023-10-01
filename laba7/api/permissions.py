from api.models import Token
from api.exceptions import InvalideToken


def validate_token(token):
    try:
        token_exist = Token.objects.filter(token=token).exists()
        if not token_exist:
            raise InvalideToken
    except:
        raise InvalideToken
