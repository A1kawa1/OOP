from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

from api.models import Task
from api.permissions import AuthorPermissions
from api.serializers import TaskSerializer

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorPermissions)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NzE3NTIzLCJpYXQiOjE2OTk2MzExMjMsImp0aSI6IjFmMTA1ZjNlODAzYTRiOWJiODBmZjliYjNmMDMwZmRlIiwidXNlcl9pZCI6MX0.0uswIyO7_uX51_3NVKJFVsm4zTbPKZyB34h-Ms4C_XM
