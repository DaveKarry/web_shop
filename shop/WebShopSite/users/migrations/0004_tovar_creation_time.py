# Generated by Django 3.1.4 on 2020-12-08 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201206_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='creation_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
