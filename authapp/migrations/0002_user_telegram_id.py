# Generated by Django 4.2.3 on 2023-08-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram_id",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="ID Телеграм"
            ),
        ),
    ]
