# Generated by Django 3.1.4 on 2020-12-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20201224_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
