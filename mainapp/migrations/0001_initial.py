# Generated by Django 4.2.3 on 2024-03-18 17:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapp.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GetHelp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="имя")),
                ("surname", models.CharField(max_length=100, verbose_name="фамилия")),
                (
                    "city",
                    models.CharField(max_length=100, verbose_name="город проживания"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="эл почта"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=20,
                        validators=[mainapp.models.validate_phone],
                        verbose_name="телефон в формате +7xxxxxxxxxx",
                    ),
                ),
                ("text", models.TextField(verbose_name="опиcание ситуации")),
                (
                    "agreed",
                    models.BooleanField(
                        default=True,
                        verbose_name="я согласен на обработку персональных данных",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запрос на помощь",
                "verbose_name_plural": "Запросы на помощь",
            },
        ),
        migrations.CreateModel(
            name="GiveHelp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="имя")),
                ("surname", models.CharField(max_length=100, verbose_name="фамилия")),
                (
                    "age",
                    models.IntegerField(
                        default=18,
                        validators=[mainapp.models.validate_age],
                        verbose_name="возраст",
                    ),
                ),
                (
                    "city",
                    models.CharField(max_length=100, verbose_name="город проживания"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="эл почта"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=20,
                        validators=[mainapp.models.validate_phone],
                        verbose_name="телефон в формате +7xxxxxxxxxx",
                    ),
                ),
                (
                    "schedule",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("2-3 часа в неделю", "2-3 часа в неделю"),
                            ("4-7 часов в неделю", "4-7 часов в неделю"),
                            ("Более 7 часов в неделю", "Более 7 часов в неделю"),
                        ],
                        max_length=64,
                        verbose_name="готовность посвящать время (в неделю)",
                    ),
                ),
                (
                    "help",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Деньгами", "Деньгами"),
                            ("Вещами", "Вещами"),
                            ("Участие", "Участие"),
                            ("Все варианты возможны", "Все варианты возможны"),
                        ],
                        max_length=64,
                        verbose_name="варианты помощи",
                    ),
                ),
                (
                    "mobility",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("На машине", "На машине"),
                            ("Пешком", "Пешком"),
                            ("Оба варианта возможны", "Оба варианта возможны"),
                        ],
                        max_length=64,
                        verbose_name="мобильность",
                    ),
                ),
                ("text", models.TextField(verbose_name="немного о себе")),
                (
                    "agreed",
                    models.BooleanField(
                        default=True,
                        verbose_name="я согласен на обработку персональных данных",
                    ),
                ),
            ],
            options={
                "verbose_name": "Анкета волонтёра",
                "verbose_name_plural": "Анкеты волонтёров",
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="заголовок")),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("description", models.TextField(verbose_name="текст статьи")),
                ("photo", models.ImageField(blank=True, upload_to="news_photos")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="дата изменения"),
                ),
                (
                    "is_closed",
                    models.BooleanField(default=False, verbose_name="событие прошло"),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Partners",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=264, verbose_name="название партнера"),
                ),
                ("picture", models.ImageField(upload_to="partner_photos")),
                ("about", models.TextField(verbose_name="информация о партнере")),
            ],
            options={
                "verbose_name": "Партнер",
                "verbose_name_plural": "Партнеры",
            },
        ),
        migrations.CreateModel(
            name="ProjectCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=64, verbose_name="имя категории проекта"
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "description",
                    models.TextField(verbose_name="описание категории проекта"),
                ),
                ("photo", models.ImageField(blank=True, upload_to="project_photos")),
            ],
            options={
                "verbose_name": "Категория проекта",
                "verbose_name_plural": "Категории проектов",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="ReportYear",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=75, verbose_name="отчетный год")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Отчетный год",
                "verbose_name_plural": "Отчетные годы",
            },
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=75, verbose_name="название отчета"),
                ),
                (
                    "upload",
                    models.FileField(
                        upload_to="uploadsFiles/%Y/%m/%d/", verbose_name="отчетный файл"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="дата создания"
                    ),
                ),
                (
                    "year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.reportyear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отчет",
                "verbose_name_plural": "Отчеты",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="название задачи"),
                ),
                ("description", models.TextField(verbose_name="описание задачи")),
                (
                    "short_description",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name="краткое описание задачи",
                    ),
                ),
                ("photo", models.ImageField(upload_to="project_photos")),
                (
                    "purpose",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="назначение платежа"
                    ),
                ),
                (
                    "donation",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=12,
                        verbose_name="необходимая сумма",
                    ),
                ),
                (
                    "collected",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=12,
                        verbose_name="собрано",
                    ),
                ),
                (
                    "in_process",
                    models.BooleanField(default=True, verbose_name="помощь актуальна"),
                ),
                (
                    "is_closed",
                    models.BooleanField(default=False, verbose_name="помощь получена"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.projectcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="AllYouNeedIs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "name",
                    models.CharField(max_length=32, verbose_name="имя подопечного"),
                ),
                (
                    "surname",
                    models.CharField(max_length=32, verbose_name="фамилия подопечного"),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="город, регион"
                    ),
                ),
                ("description", models.TextField(verbose_name="описание проблемы")),
                (
                    "short_description",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="краткое описание проблемы",
                    ),
                ),
                ("photo", models.ImageField(upload_to="needs_photos")),
                (
                    "purpose",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="назначение платежа"
                    ),
                ),
                (
                    "donation",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=12,
                        verbose_name="необходимая сумма",
                    ),
                ),
                (
                    "collected",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=12,
                        verbose_name="собрано",
                    ),
                ),
                (
                    "in_process",
                    models.BooleanField(default=True, verbose_name="помощь актуальна"),
                ),
                (
                    "is_closed",
                    models.BooleanField(default=False, verbose_name="помощь получена"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.projectcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подопечный",
                "verbose_name_plural": "Подопечные",
                "ordering": ["id"],
            },
        ),
    ]
