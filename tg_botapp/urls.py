import tg_botapp.views as telegram
from django.urls import path

app_name = 'tg_botapp'

urlpatterns = [
    path('', telegram.index, name='index'),
]
