# Generated by Django 3.1.5 on 2021-01-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20210117_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='descr',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
