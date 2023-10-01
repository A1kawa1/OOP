from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from uuid import uuid4

from api.models import Token
from api.serializers import GoodSerializer
from api.permissions import TokenPermission
from goods.models import Good


@api_view(['GET'])
def get_token(request):
    rand_token = uuid4()

    token = Token.objects.create(
        token=rand_token
    )
    return Response(
        {'token': token.token},
        status.HTTP_200_OK
    )


class GoodPostList(viewsets.GenericViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (TokenPermission,)


class GoodList(mixins.ListModelMixin, GoodPostList):
    ...


class GoodPost(mixins.CreateModelMixin, GoodPostList):
    ...
