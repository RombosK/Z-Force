from django.urls import path
from django.views.generic import RedirectView

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

# urlpatterns = [
#     path("", views.HelloView.as_view()),
#     path("<str:word>/", views.check_kwargs),
# ]

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='home'),
    path('yandex/', RedirectView.as_view(url='https://yandex.ru/search/', query_string=True), name='yandex'),

]
