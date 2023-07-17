from django.contrib import admin
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mainapp.urls")),

]



