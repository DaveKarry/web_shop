# Generated by Django 3.1.4 on 2020-12-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20201223_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
