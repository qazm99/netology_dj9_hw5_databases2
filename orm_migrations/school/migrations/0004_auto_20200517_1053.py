# Generated by Django 3.0.5 on 2020-05-17 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teachers',
            new_name='teacher',
        ),
    ]
