from django.urls import path

from authapp.apps import AuthappConfig
from authapp.views import (CustomLoginView, CustomLogoutView, EditView,
                           RegisterView)

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/', EditView.as_view(), name='edit'),

]

