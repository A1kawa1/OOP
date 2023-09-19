from django.urls import path
from main.views import index, words_list, add_word, download_txt

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('words_list/', words_list, name='words_list'),
    path('add_word/', add_word, name='add_word'),
    path('download_txt/', download_txt, name='download_txt')
]
