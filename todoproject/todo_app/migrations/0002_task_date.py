# Generated by Django 4.2 on 2023-08-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1990-06-09'),
            preserve_default=False,
        ),
    ]
