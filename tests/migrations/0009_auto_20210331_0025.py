# Generated by Django 3.1.7 on 2021-03-30 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_auto_20210331_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longwriteanswer',
            old_name='answer',
            new_name='text',
        ),
    ]
