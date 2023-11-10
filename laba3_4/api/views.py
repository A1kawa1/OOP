from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from datetime import datetime
import jwt

from api.permissions import authenticate_user, ReadOrAdminPostOrAuthPatch
from api.serializers import UserSerializer


@api_view(['POST'])
def login(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        role = serializer.data.get('role')
        if not authenticate_user(username, password):
            return Response(
                {
                    'detail': 'invalid credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {
                'access_token': jwt.encode(
                    {
                        'username': username,
                        'password': password,
                        'role': role,
                        'start_date': datetime.now().strftime('%Y-%m-%d')
                    },
                    'secret',
                    algorithm="HS256"
                )
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtectedResource(APIView):
    permission_classes = [ReadOrAdminPostOrAuthPatch]
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     elif self.request.method == 'POST':
    #         return [AdminPostPermission()]
    #     elif self.request.method == 'PATCH':
    #         return [AuthPatchPermission()]

    def get(self, request):
        return Response({'permission': True})

    def post(self, request):
        return Response({'permission': True})

    def patch(self, request):
        return Response({'permission': True})

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJwYXNzd29yZCI6IjEyMzEyMzEyMzEiLCJyb2xlIjoidXNlciIsInN0YXJ0X2RhdGUiOiIyMDIzLTExLTEwIn0.gOL2whvRPNfHdFqvWSJL7Ulev98uYOZFKpgemxlqgJE
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJwYXNzd29yZCI6IjEyMzEyMzEyMzEiLCJyb2xlIjoiYWRtaW4iLCJzdGFydF9kYXRlIjoiMjAyMy0xMS0xMCJ9.RaE3IWw9dD47m0WQSKkmVt0NmiuKZFGsxHK7ATtLy6U
