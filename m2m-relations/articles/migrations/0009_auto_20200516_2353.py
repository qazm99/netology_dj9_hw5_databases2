# Generated by Django 3.0.5 on 2020-05-16 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_theme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='theme',
            new_name='scope',
        ),
    ]
