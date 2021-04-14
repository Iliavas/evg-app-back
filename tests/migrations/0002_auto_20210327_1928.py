# Generated by Django 3.1.7 on 2021-03-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theory', models.TextField()),
                ('practise', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]