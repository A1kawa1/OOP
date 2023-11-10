from django.urls import path

from api.views import login, protected_resource


app_name = 'api'
urlpatterns = [
    path('login/', login, name='login'),
    path(
        'protected_resource/',
        protected_resource,
        name='protected_resource'
    )
]
