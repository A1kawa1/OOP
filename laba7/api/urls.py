from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import get_token, GoodList, GoodPost


router = DefaultRouter()
router.register('goods', GoodList, basename='goods_list')
router.register('new_good', GoodPost, basename='goods_post')

urlpatterns = [
    path('get_token/', get_token),
    path('', include(router.urls))
]
