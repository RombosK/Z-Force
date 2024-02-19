from django.contrib import admin

from mainapp.models import News, ProjectCategory, Project, AllYouNeedIs

# Регистрация моделей в админке
admin.site.register(News)
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(AllYouNeedIs)
