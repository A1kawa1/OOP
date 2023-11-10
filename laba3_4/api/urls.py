from django.urls import path

from api.views import login, ProtectedResource


app_name = 'api'
urlpatterns = [
    path('login/', login, name='login'),
    path(
        'protected_resource/',
        ProtectedResource.as_view(),
        name='protected_resource'
    )
]
