# Generated by Django 3.0.5 on 2020-05-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20200517_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.AddField(
            model_name='article',
            name='thems',
            field=models.ManyToManyField(related_name='articles', related_query_name='scopes', through='articles.Theming', to='articles.Theme'),
        ),
    ]
