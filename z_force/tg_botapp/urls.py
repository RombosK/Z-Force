from django.urls import path
import z_force.tg_botapp.views as telegram


app_name = 'tg_botapp'

urlpatterns = [
    path('', telegram.index, name='index'),
]
