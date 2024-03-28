from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from authapp.models import User
from config.settings import BASE_DIR
from django.conf import settings


class Images(models.Model):
    image = models.ImageField(verbose_name='фотоальбом', upload_to='images/%Y/%m/%d/', blank=True)
    post = models.ForeignKey('News', verbose_name='для новости', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии для слайдера новостей'


# Модель новостей
class News(models.Model):
    name = models.CharField(verbose_name='заголовок', max_length=64)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='news_photos', blank=True)
    photo_image = models.ForeignKey('Images', on_delete=models.CASCADE, blank=True, null=True, verbose_name='доп фото')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата создания', editable=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения', editable=False)
    is_closed = models.BooleanField(default=False, verbose_name='событие прошло')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


# Модель проектов фонда (категории для задач)
class ProjectCategory(models.Model):
    name = models.CharField(verbose_name='имя категории проекта', max_length=64)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(verbose_name='описание категории проекта')
    photo = models.ImageField(upload_to='project_photos', blank=True)

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('project_category', kwargs={'post_slug': self.slug})

    def __str__(self):
        return f'{self.name}'


class ImagesProject(models.Model):
    image = models.ImageField(verbose_name='фотоальбом', upload_to='images/%Y/%m/%d/', blank=True)
    post = models.ForeignKey('Project', verbose_name='для Проектов', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии для слайдера Задачи'


# Модель конкретного проекта (задачи)
class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(verbose_name='название задачи', max_length=128)
    description = models.TextField(verbose_name='описание задачи')
    short_description = models.CharField(verbose_name='краткое описание задачи', max_length=255, blank=True)
    photo = models.ImageField(upload_to='project_photos')
    purpose = models.CharField(verbose_name='назначение платежа', max_length=64, blank=True)
    donation = models.DecimalField(verbose_name='необходимая сумма', max_digits=12, decimal_places=2, default=0)
    collected = models.DecimalField(verbose_name='собрано', max_digits=12, decimal_places=2, default=0)
    in_process = models.BooleanField(default=True, verbose_name='помощь актуальна')
    is_closed = models.BooleanField(default=False, verbose_name='помощь получена')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.category}'


class ImagesAllYouNeedIs(models.Model):
    image = models.ImageField(verbose_name='фотоальбом', upload_to='images/AllYouNeedIs/%Y/%m/%d/', blank=True)
    post = models.ForeignKey('AllYouNeedIs', verbose_name='для Подопечных', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии для слайдера Подопечных'


# Модель подопечных
class AllYouNeedIs(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(verbose_name='имя подопечного', max_length=32)
    surname = models.CharField(verbose_name='фамилия подопечного', max_length=32)
    city = models.CharField(verbose_name='город, регион', max_length=64, blank=True)
    birthdate = models.CharField(verbose_name='Год рождения', max_length=4, null=True)
    description = models.TextField(verbose_name='описание проблемы')
    short_description = models.CharField(verbose_name='краткое описание проблемы', max_length=128, blank=True)
    # name_for_payment = models.CharField(verbose_name='напишите имя в дательном пажеде', max_length=32, blank=True)
    photo = models.ImageField(upload_to='needs_photos')
    purpose = models.CharField(verbose_name='назначение платежа', max_length=64, blank=True)
    donation = models.DecimalField(verbose_name='необходимая сумма', max_digits=12, decimal_places=0, default=0)
    collected = models.DecimalField(verbose_name='собрано', max_digits=12, decimal_places=0, default=0)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата создания', editable=True)
    in_process = models.BooleanField(default=True, verbose_name='помощь актуальна')
    is_closed = models.BooleanField(default=False, verbose_name='помощь получена')

    class Meta:
        verbose_name = 'Подопечный'
        verbose_name_plural = 'Подопечные'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} {self.surname}'


from django.core.exceptions import ValidationError
import phonenumbers


# Валидатор для строки с указанием возраста
def validate_age(value):
    if value < 18:
        raise ValidationError('Анкету отправить нельзя. Вы слишком молоды')
    if value > 100:
        raise ValidationError('Шутить изволите?')


# Валидатор для телефонной строки в анкете
def validate_phone(value):
    try:
        parsed_phone = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_phone):
            raise ValidationError("Некорректный формат номера телефона")
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError("Некорректный формат номера телефона")


# Модель анкеты волонтера
# class GiveHelp(models.Model):
#     TIME_1 = '2-3 часа в неделю'
#     TIME_2 = '4-7 часов в неделю'
#     TIME_3 = 'Более 7 часов в неделю'
#
#     SCHEDULE = (
#         (TIME_1, '2-3 часа в неделю'),
#         (TIME_2, '4-7 часов в неделю'),
#         (TIME_3, 'Более 7 часов в неделю')
#     )
#
#     CAR = 'На машине'
#     WALK = 'Пешком'
#     BOTH = 'Оба варианта возможны'
#
#     MOBILITY = (
#         (CAR, 'На машине'),
#         (WALK, 'Пешком'),
#         (BOTH, 'Оба варианта возможны')
#     )
#
#     MONEY = 'Деньгами'
#     THINGS = 'Вещами'
#     INVOLVEMENT = 'Участие'
#     BOTH = 'Все варианты возможны'
#
#     HELP = (
#         (MONEY, 'Деньгами'),
#         (THINGS, 'Вещами'),
#         (INVOLVEMENT, 'Участие'),
#         (BOTH, 'Все варианты возможны')
#     )
#
#     name = models.CharField(verbose_name='имя', max_length=100)
#     surname = models.CharField(verbose_name='фамилия', max_length=100)
#     age = models.IntegerField(verbose_name='возраст', default=18, validators=[validate_age])
#     city = models.CharField(verbose_name='город проживания', max_length=100)
#     email = models.EmailField(verbose_name='эл почта', unique=True)
#     phone = models.CharField(verbose_name='телефон в формате +7xxxxxxxxxx', max_length=20, validators=[validate_phone])
#     schedule = models.CharField(verbose_name='готовность посвящать время (в неделю)', choices=SCHEDULE, max_length=64, blank=True)
#     help = models.CharField(verbose_name='варианты помощи', choices=HELP, max_length=64, blank=True)
#     mobility = models.CharField(verbose_name='мобильность', choices=MOBILITY, max_length=64, blank=True)
#     text = models.TextField(verbose_name='немного о себе')
#     agreed = models.BooleanField(verbose_name='я согласен на обработку персональных данных', blank=False, default=True)
#
#     def __str__(self):
#         return f'{self.name} - {self.surname} - {self.city}'
#
#     class Meta:
#         verbose_name = 'Анкета волонтёра'
#         verbose_name_plural = 'Анкеты волонтёров'

class GiveHelp(models.Model):
    TIME_1 = '2-3 часа в неделю'
    TIME_2 = '4-7 часов в неделю'
    TIME_3 = 'Более 7 часов в неделю'

    SCHEDULE = (
        (TIME_1, '2-3 часа в неделю'),
        (TIME_2, '4-7 часов в неделю'),
        (TIME_3, 'Более 7 часов в неделю')
    )

    CAR = 'На машине'
    WALK = 'Пешком'
    BOTH = 'Оба варианта возможны'

    MOBILITY = (
        (CAR, 'На машине'),
        (WALK, 'Пешком'),
        (BOTH, 'Оба варианта возможны')
    )

    MONEY = 'Деньгами'
    THINGS = 'Вещами'
    INVOLVEMENT = 'Участие'
    BOTH = 'Все варианты возможны'

    HELP = (
        (MONEY, 'Деньгами'),
        (THINGS, 'Вещами'),
        (INVOLVEMENT, 'Участие'),
        (BOTH, 'Все варианты возможны')
    )

    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    city = models.CharField(verbose_name='Город проживания', max_length=100)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20,
                             validators=[validate_phone])
    text_1 = models.TextField(verbose_name='Немного о себе')
    text_2 = models.TextField(verbose_name='Как я хочу помочь')

    schedule = models.CharField(verbose_name='сколько времени в неделю готовы уделять', choices=SCHEDULE, max_length=64,
                                blank=True)
    help = models.CharField(verbose_name='варианты помощи', choices=HELP, max_length=64, blank=True)
    mobility = models.CharField(verbose_name='мобильность', choices=MOBILITY, max_length=64, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.text_1} - {self.text_2}'

    class Meta:
        verbose_name = 'Анкета волонтёра'
        verbose_name_plural = 'Анкеты волонтёров'


# Модель анкеты на помощь
class GetHelp(models.Model):
    # name = models.CharField(verbose_name='имя', max_length=100)
    name = models.CharField(verbose_name='Имя', max_length=100)

    surname = models.CharField(verbose_name='фамилия', max_length=100)
    city = models.CharField(verbose_name='город проживания', max_length=100)
    email = models.EmailField(verbose_name='e-mail', unique=True)
    phone = models.CharField(verbose_name='телефон', max_length=20, validators=[validate_phone])
    text = models.TextField(verbose_name='опиcание ситуации')
    agreed = models.BooleanField(verbose_name='я согласен на обработку персональных данных', blank=False, default=True)

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.city}'

    class Meta:
        verbose_name = 'Запрос на помощь'
        verbose_name_plural = 'Запросы на помощь'


# Модель партнера
class Partners(models.Model):
    title = models.CharField(verbose_name='название партнера', max_length=264)
    picture = models.ImageField(upload_to='partner_photos')
    about = models.TextField(verbose_name='информация о партнере')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


# Модель готового отчетного периода для модели отчета
class ReportYear(models.Model):
    name = models.CharField(max_length=75, verbose_name='отчетный год')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата создания', editable=True)

    class Meta:
        verbose_name = 'Отчетный год'
        verbose_name_plural = 'Отчетные годы'

    def __str__(self):
        return f'{self.name}'


# fs = FileSystemStorage(base_url=str(settings.MEDIA_ROOT) + "uploads/%Y/%m/%d/")
# print(fs)

# Модель для страницы с отчетами
class Report(models.Model):
    name = models.CharField(max_length=75, verbose_name='название отчета')
    year = models.ForeignKey(ReportYear, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploadsFiles/%Y/%m/%d/', verbose_name='отчетный файл')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата создания', editable=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return "user_{0}/{1}".format(instance.user.id, filename)
