# Generated by Django 4.1.5 on 2023-03-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-02-11'),
            preserve_default=False,
        ),
    ]
