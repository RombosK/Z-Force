from django.urls import path
from mainapp.apps import MainappConfig
from mainapp import views

app_name = MainappConfig.name

urlpatterns = [
    path("", views.hello_Z),
    path("<str:word>/", views.check_kwargs),
]


