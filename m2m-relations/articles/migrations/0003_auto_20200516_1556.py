# Generated by Django 3.0.5 on 2020-05-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200516_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterField(
            model_name='theming',
            name='is_main',
            field=models.BooleanField(verbose_name='Основная тема'),
        ),
    ]
