from mainapp.models import News, ProjectCategory, Project, AllYouNeedIs, RequestVolunteer, RequestCharity
from django.contrib import admin


# Регистрация моделей в админке
# admin.site.register(News)
# admin.site.register(Project)
# admin.site.register(ProjectCategory)
# admin.site.register(AllYouNeedIs)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_closed')
    list_per_page = 10
    list_filter = ('name', 'description', 'created_at')
    search_fields = ('name', 'description', 'created_at')
    show_full_result_count = False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'category', 'donation')
    list_per_page = 10
    list_filter = ('name', 'short_description', 'category')
    search_fields = ('name', 'short_description', 'category')
    show_full_result_count = False


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_per_page = 10
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    show_full_result_count = False


@admin.register(AllYouNeedIs)
class AllYouNeedIsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'category', 'city', 'short_description', 'in_process', 'is_closed')
    list_per_page = 10
    list_filter = ('name', 'surname', 'category', 'city', 'in_process', 'is_closed')
    search_fields = ('name', 'surname', 'city', 'short_description', 'in_process', 'is_closed')
    show_full_result_count = False


@admin.register(RequestVolunteer)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'email', 'phone', 'text')
    list_per_page = 10
    list_filter = ('last_name', 'city', 'email', 'phone')
    search_fields = ('last_name', 'city', 'email', 'phone')
    show_full_result_count = False


@admin.register(RequestCharity)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'first_name', 'last_name', 'city', 'email', 'phone', 'text')
    list_per_page = 10
    list_filter = ('last_name', 'city', 'email', 'phone')
    search_fields = ('last_name', 'city', 'email', 'phone')
    show_full_result_count = False




