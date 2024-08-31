from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('targets/', views.TargetsView.as_view(), name='targets'),
    path('history/', views.HistoryView.as_view(), name='history'),

    path('projects_category/', views.ProjectCategoryView.as_view(), name='projects_category'),
    path('allyouneedis/', views.AllYouNeedIsView.as_view(), name='allyouneedis'),
    path('donation/', views.DonationView.as_view(), name='donation'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('yandex/', RedirectView.as_view(url='https://yandex.ru/search/', query_string=True), name='yandex'),
    path('offero/', views.OfferoView.as_view(), name='offero'),
    path('personal_data/', views.PersonalDataView.as_view(), name='personal_data'),
    path('legal/', views.LegalView.as_view(), name='legal'),
    path('partners/', views.PartnersView.as_view(), name='partners'),
    path('give_help/', views.GiveHelpView.as_view(), name='give_help'),
    path('get_help/', views.GetHelpView.as_view(), name='get_help'),
    path('success/', TemplateView.as_view(template_name='mainapp/success.html'), name='success'),
    path('news/<slug:post_slug>/', views.NewsDetailView.as_view(), name='news_post'),
    path('projects_category/<int:pk>/', views.ProjectView.as_view(), name='projects'),
    path('projects_post/<slug:slug>/', views.ProjectDetailView.as_view(), name='projects_post'),
    path('allyouneedis/<slug:slug>/', views.AllYouNeedIsDetailView.as_view(), name='allyouneedis_post'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('vid/', views.VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video_detail'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)