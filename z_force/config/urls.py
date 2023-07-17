from django.contrib import admin
from django.urls import path
from adminapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.hello_Z),
    path("<str:word>/", views.check_kwargs),
]



