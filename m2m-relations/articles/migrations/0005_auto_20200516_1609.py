# Generated by Django 3.0.5 on 2020-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200516_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='theme',
            field=models.ManyToManyField(to='articles.Theme', verbose_name='Тема'),
        ),
    ]
