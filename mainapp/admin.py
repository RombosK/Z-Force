from mainapp.models import News, ProjectCategory, Project, AllYouNeedIs, GiveHelp, GetHelp, Partners, Report, ReportYear
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


@admin.register(GiveHelp)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'first_name', 'last_name', 'city', 'email', 'phone', 'text')
    list_per_page = 10
    list_filter = ('last_name', 'city', 'email', 'phone')
    search_fields = ('last_name', 'city', 'email', 'phone')
    show_full_result_count = False


@admin.register(GetHelp)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'email', 'phone', 'subject', 'text')
    list_per_page = 10
    list_filter = ('last_name', 'city', 'email', 'phone')
    search_fields = ('last_name', 'city', 'email', 'phone')
    show_full_result_count = False


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'about')
    list_per_page = 10
    list_filter = ('title', 'about')
    search_fields = ('title', 'about')
    show_full_result_count = False


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'upload', 'created_at',)
    list_per_page = 12
    list_filter = ('name', 'upload', 'created_at')
    search_fields = ('name', 'upload', 'created_at')
    show_full_result_count = False


@admin.register(ReportYear)
class ReportYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_per_page = 3
    list_filter = ('name', 'created_at')
    search_fields = ('name','created_at')
    show_full_result_count = False
