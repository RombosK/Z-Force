from mainapp.models import News, ProjectCategory, Project, AllYouNeedIs, GiveHelp, GetHelp, Partners, Report, \
    ReportYear, Images, ImagesMany
from django.contrib import admin


# Регистрация моделей в админке

# class Image(admin.StackedInline):
#     model = Images
#
#     fields = ["image", "name"]
#     max_num = 10
#     extra = 0


class ImagesNewsInline(admin.StackedInline):
    model = ImagesMany
    fields = ["image", ]
    max_num = 10
    extra = 0
    fk_name = "news_image"


class ImagesProjectInline(admin.StackedInline):
    model = ImagesMany
    fields = ["image",]
    max_num = 10
    extra = 0
    fk_name = "projects_image"


class ImagesAllyouneedisInline(admin.StackedInline):
    model = ImagesMany
    fields = ["image", ]
    max_num = 10
    extra = 0
    fk_name = "allyouneedis_image"


# class ImagesProjectInline(admin.StackedInline):
#     model = Images
#     max_num = 10
#     extra = 0
#
#
# class ImagesAllYouNeedIsInline(admin.StackedInline):
#     model = Images
#     max_num = 10
#     extra = 0


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_closed')
    list_per_page = 10
    list_filter = ('name', 'description', 'created_at')
    search_fields = ('name', 'description', 'created_at')
    show_full_result_count = False
    inlines = [ImagesNewsInline, ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    # prepopulated_fields = {
    #     'name': ('image',)
    # }
    list_per_page = 25
    list_filter = ('image', 'name')
    search_fields = ('image', 'name')


# @admin.register(ImagesProject)
# class ImagesProjectAdmin(admin.ModelAdmin):
#     list_display = ('image',)
#     list_per_page = 10
#     list_filter = ('image',)
#     search_fields = ('images',)
#
#
# @admin.register(ImagesAllYouNeedIs)
# class ImagesAllYouNeedIsAdmin(admin.ModelAdmin):
#     list_display = ('image',)
#     list_per_page = 10
#     list_filter = ('image',)
#     search_fields = ('images',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'category', 'donation')
    prepopulated_fields = {
        'slug': ('name', 'category')
    }
    list_per_page = 10
    list_filter = ('name', 'short_description', 'category')
    search_fields = ('name', 'short_description', 'category')
    show_full_result_count = False
    inlines = [ImagesProjectInline, ]


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = ('name', 'description')
    list_per_page = 10
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    show_full_result_count = False


@admin.register(AllYouNeedIs)
class AllYouNeedIsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', 'surname', 'city')
    }
    list_display = ('name', 'surname', 'city', 'short_description', 'in_process', 'is_closed')
    list_per_page = 10
    list_filter = ('name', 'surname', 'city', 'in_process', 'is_closed')
    search_fields = ('name', 'surname', 'city', 'short_description', 'in_process', 'is_closed')
    show_full_result_count = False
    inlines = [ImagesAllyouneedisInline, ]


@admin.register(GiveHelp)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'email', 'phone', 'text_1', 'text_2')
    list_per_page = 10
    list_filter = ('last_name', 'city', 'email', 'phone')
    search_fields = ('last_name', 'city', 'email', 'phone')
    show_full_result_count = False


@admin.register(GetHelp)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'city', 'email', 'phone', 'text')
    list_per_page = 10
    list_filter = ('surname', 'city', 'email', 'phone')
    search_fields = ('surname', 'city', 'email', 'phone')
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
