from django.db import models


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

    def __str__(self):
        return f'{self.id} - {self.name}'


# Модель проектов фонда (категории благотворительности)
class ProjectCategory(models.Model):
    name = models.CharField(verbose_name='имя проекта', max_length=64)
    description = models.TextField(verbose_name='описание проекта')
    photo = models.ImageField(upload_to='project_photos', blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name}'


# Модель конкретного проекта
class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=128)
    description = models.TextField(verbose_name='описание задачи')
    short_description = models.CharField(verbose_name='краткое описание задачи', max_length=64, blank=True)
    photo = models.ImageField(upload_to='project_photos')
    donation = models.DecimalField(verbose_name='необходимая сумма', max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

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

    def __str__(self):
        return f'{self.name} {self.surname} - {self.category.name}'