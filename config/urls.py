from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url='home/')),
    path("home/", include('mainapp.urls', namespace='home')),
    path("authapp/", include('authapp.urls', namespace='authapp')),
    path("__debug__/", include("debug_toolbar.urls")),


]
