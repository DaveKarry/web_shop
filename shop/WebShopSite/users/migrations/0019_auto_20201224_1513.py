# Generated by Django 3.1.4 on 2020-12-24 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20201224_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='count',
        ),
        migrations.RemoveField(
            model_name='tovar',
            name='creation_time',
        ),
    ]
