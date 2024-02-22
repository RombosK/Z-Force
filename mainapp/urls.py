from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.conf.urls.static import static
from django.conf import settings
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('allyouneedis/', views.AllYouNeedIsView.as_view(), name='allyouneedis'),
    path('donation/', views.DonationView.as_view(), name='donation'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('yandex/', RedirectView.as_view(url='https://yandex.ru/search/', query_string=True), name='yandex'),
    path('offero/', views.OfferoView.as_view(), name='offero'),
    path('personal_data/', views.PersonalDataView.as_view(), name='personal_data'),
    path('legal/', views.LegalView.as_view(), name='legal'),
    path('request/', views.RequestEditView.as_view(), name='request'),
    path('success/', TemplateView.as_view(template_name='mainapp/success.html'), name='success'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
