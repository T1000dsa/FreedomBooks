# Generated by Django 5.1.6 on 2025-03-07 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freedombooks_core', '0002_bookmodel_text_file_hook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='text_file_hook',
        ),
        migrations.AddField(
            model_name='textmodel',
            name='text_file_hook',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='freedombooks_core.uploadfiles'),
        ),
    ]
