# Generated by Django 3.1.4 on 2020-12-03 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('count', models.IntegerField()),
                ('short_description', models.CharField(max_length=100)),
                ('full_description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('category', models.ManyToManyField(to='users.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Users_purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tovars_in_purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tovar')),
                ('users_purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users_purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('index', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
