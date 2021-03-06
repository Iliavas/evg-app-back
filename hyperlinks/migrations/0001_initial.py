# Generated by Django 3.1.5 on 2021-01-20 17:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisations', '0005_auto_20210120_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='HyperLink',
            fields=[
                ('link', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('child', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.child')),
                ('organ', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.organisator')),
                ('teacher', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.teacher')),
            ],
        ),
    ]
