from django.core.validators import RegexValidator
from django.db import models
from authapp.models import User


# Модель новостей
class News(models.Model):
    name = models.CharField(verbose_name='заголовок', max_length=64)
    description = models.TextField(verbose_name='текст статьи')
    photo = models.ImageField(upload_to='news_photos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения', editable=False)
    is_closed = models.BooleanField(default=False, verbose_name='событие прошло')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'


# Модель проектов фонда (категории благотворительности)
class ProjectCategory(models.Model):
    name = models.CharField(verbose_name='имя категории проекта', max_length=64)
    description = models.TextField(verbose_name='описание категории проекта')
    photo = models.ImageField(upload_to='project_photos', blank=True)

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
        return f'{self.name}'


# Модель конкретного проекта
class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название проекта', max_length=128)
    description = models.TextField(verbose_name='описание проекта')
    short_description = models.CharField(verbose_name='краткое описание проекта', max_length=64, blank=True)
    photo = models.ImageField(upload_to='project_photos')
    donation = models.DecimalField(verbose_name='необходимая сумма', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name} - {self.category.name}'


# Модель подопечных
class AllYouNeedIs(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя нуждающегося', max_length=32)
    surname = models.CharField(verbose_name='фамилия нуждающегося', max_length=32)
    city = models.CharField(verbose_name='город, регион', max_length=64, blank=True)
    description = models.TextField(verbose_name='описание проблемы')
    short_description = models.CharField(verbose_name='краткое описание проблемы', max_length=128, blank=True)
    solution = models.TextField(verbose_name='описание решения')
    photo = models.ImageField(upload_to='needs_photos')
    donation = models.DecimalField(verbose_name='необходимая сумма', max_digits=12, decimal_places=2, default=0)
    collected = models.DecimalField(verbose_name='собрано', max_digits=12, decimal_places=2, default=0)
    in_process = models.BooleanField(default=True, verbose_name='помощь актуальна')
    is_closed = models.BooleanField(default=False, verbose_name='помощь получена')

    class Meta:
        verbose_name = 'Подопечный'
        verbose_name_plural = 'Подопечные'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} {self.surname} - {self.category.name}'


from django.core.exceptions import ValidationError
import phonenumbers


# Валидатор для телефонной строки в анкете
def validate_phone(value):
    try:
        parsed_phone = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_phone):
            raise ValidationError("Некорректный номер телефона")
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError("Некорректный номер телефона")


# Модель анкеты волонтера
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

    company_name = models.CharField(help_text='если вы являетесь юр лицом', verbose_name='название юр лица', max_length=128, blank=True)
    first_name = models.CharField(verbose_name='имя', max_length=100)
    last_name = models.CharField(verbose_name='фамилия', max_length=100)
    birthday = models.DateField(verbose_name="дата рождения", blank=True, null=True)
    country = models.CharField(verbose_name='страна проживания', max_length=100, null=True)
    city = models.CharField(verbose_name='город проживания', max_length=100)
    email = models.EmailField(verbose_name='эл почта для связи', unique=True)
    phone = models.CharField(help_text='телефон в формате +7xxxxxxxxxx', verbose_name='телефон для связи', max_length=20, validators=[validate_phone])
    social_network = models.CharField(verbose_name='ссылка на социальную сеть', max_length=100, blank=True)
    schedule = models.CharField(verbose_name='сколько времени в неделю готовы уделять', choices=SCHEDULE, max_length=64, blank=True)
    help = models.CharField(verbose_name='варианты помощи', choices=HELP, max_length=64, blank=True)
    mobility = models.CharField(verbose_name='мобильность', choices=MOBILITY, max_length=64, blank=True)
    text = models.TextField(verbose_name='немного о себе')
    agreed = models.BooleanField(verbose_name='я согласен на обработку персональных данных', default=False)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.text}'

    class Meta:
        verbose_name = 'Анкета волонтёра'
        verbose_name_plural = 'Анкеты волонтёров'


# Модель анкеты на помощь
class GetHelp(models.Model):
    first_name = models.CharField(verbose_name='имя', max_length=100)
    last_name = models.CharField(verbose_name='фамилия', max_length=100)
    city = models.CharField(verbose_name='город проживания', max_length=100)
    email = models.EmailField(verbose_name='эл почта для связи', unique=True)
    phone = models.CharField(help_text='телефон в формате +7xxxxxxxxxx', verbose_name='телефон для связи', max_length=20, validators=[validate_phone])
    social_network = models.CharField(verbose_name='ссылка на социальную сеть', max_length=100, blank=True)
    subject = models.CharField(verbose_name='тема / заголовок', max_length=100)
    text = models.TextField(verbose_name='описание проблемы')
    agreed = models.BooleanField(verbose_name='я согласен на обработку персональных данных', default=False)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.text}'

    class Meta:
        verbose_name = 'Запрос на помощь'
        verbose_name_plural = 'Запросы на помощь'


# Модель партнера
class Partners(models.Model):
    title = models.CharField(verbose_name='название партнера', max_length=264)
    about = models.TextField(verbose_name='информация о партнере')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'