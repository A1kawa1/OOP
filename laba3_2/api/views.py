from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import jwt

from api.permissions import authenticate_user, ProtectedResourcePermission
from api.serializers import UserSerializer


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

        return Response(
            {
                'access_token': jwt.encode(
                    {
                        'username': username,
                        'password': password,
                        'start_date': datetime.now().strftime('%Y-%m-%d')
                    },
                    'secret',
                    algorithm="HS256"
                )
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([ProtectedResourcePermission])
def protected_resource(request):
    return Response({'permission': True})

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJ0ZXN0IiwicGFzc3dvcmQiOiIxMjMxMjMxMjMxIiwicm9sZSI6ImFkbWluIiwic3RhcnRfZGF0ZSI6IjIwMjMtMTEtMDkifQ.XI2RRIh0ZttbkZuJNogQgvOO4MuBkOhA1KT8ModmqwU
