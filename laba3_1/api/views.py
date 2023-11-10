from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt

from api.serializers import UserSerializer
from api.permissions import authenticate_user


@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        if not authenticate_user(username, password):
            return Response(
                {'detail': 'invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        response = Response(
            {'detail': 'session_token is set'},
            status=status.HTTP_200_OK
        )
        session_token = jwt.encode(
            {
                'username': username,
                'password': password,
            },
            'secret',
            algorithm="HS256"
        )
        cache.set(
            session_token,
            1,
            timeout=10
        )
        response.set_cookie(
            'session_token',
            session_token,
            secure=True,
            httponly=True
        )

        return response

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user(request):
    session_token = request.COOKIES.get('session_token')
    if session_token is None or cache.get(session_token) is None:
        return Response(
            {'detail': 'Unauthorized'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        data = jwt.decode(session_token, 'secret', algorithms=['HS256'])
        username = data.get('username')

        if username is None:
            raise Exception
    except:
        return Response(
            {'detail': 'Unauthorized'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    return Response(
        {'username': username},
        status=status.HTTP_200_OK
    )
