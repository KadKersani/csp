# Generated by Django 3.0.8 on 2021-04-20 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vrp', '0002_task_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='visited',
        ),
    ]
