# Generated by Django 3.1.7 on 2021-05-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='material',
            name='state',
            field=models.TextField(blank=True),
        ),
    ]
