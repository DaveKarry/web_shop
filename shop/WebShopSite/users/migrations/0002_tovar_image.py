# Generated by Django 3.1.4 on 2020-12-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='image',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]
