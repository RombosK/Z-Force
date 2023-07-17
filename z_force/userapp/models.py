from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(models.Model):
    username = models.CharField(max_length=16, verbose_name='Ник')
    telegram_id = models.PositiveIntegerField(verbose_name='ID Телеграм', **NULLABLE)
    email = models.EmailField(verbose_name='email', **NULLABLE)
    birthdate = models.DateField(verbose_name='Дата рождения', null=True)
    is_moderator = models.BooleanField(default=False, verbose_name='Модератор')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

