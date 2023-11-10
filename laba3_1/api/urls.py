from django.urls import path

from api.views import login, user


app_name = 'api'
urlpatterns = [
    path('login/', login, name='login'),
    path('user/', user, name='user')
]
