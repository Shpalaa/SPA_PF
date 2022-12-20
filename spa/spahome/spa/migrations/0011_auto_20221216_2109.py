# Generated by Django 3.2.16 on 2022-12-16 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0010_body_care_time_create_body_care_time_update_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MY_CHOICES', models.CharField(choices=[('KP', 'Красная Поляна'), ('PX', 'Роза Хутор'), ('GZ', 'Горно-туристический центр ПАО «Газпром»')], max_length=2)),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('number', models.FloatField(max_length=14)),
            ],
        ),
        migrations.AlterField(
            model_name='body_care',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 105838), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='body_care',
            name='time_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 105838), verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='rituals',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 104808), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='rituals',
            name='time_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 104808), verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='save_menu',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 106839), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='save_menu',
            name='time_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 106839), verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='sea_spa_bc',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 106839), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='sea_spa_bc',
            name='time_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 106839), verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='sea_spa_rt',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 105838), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='sea_spa_rt',
            name='time_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 21, 9, 52, 105838), verbose_name='Время изменения'),
        ),
    ]
