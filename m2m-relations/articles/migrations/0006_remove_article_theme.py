# Generated by Django 3.0.5 on 2020-05-16 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200516_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='theme',
        ),
    ]
