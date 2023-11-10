from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import TaskViewSet


router = DefaultRouter()
router.register('todos', TaskViewSet, basename='todos')

app_name = 'api'
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
