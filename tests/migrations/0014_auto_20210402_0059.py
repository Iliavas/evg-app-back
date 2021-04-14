# Generated by Django 3.1.7 on 2021-04-01 21:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0013_audiodialog'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiodialog',
            name='custom_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='readandsaytext',
            name='custom_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='writetask',
            name='custom_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False),
        ),
    ]
