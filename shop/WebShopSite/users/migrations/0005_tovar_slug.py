# Generated by Django 3.1.4 on 2020-12-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_tovar_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='slug',
            field=models.SlugField(default='test1'),
            preserve_default=False,
        ),
    ]