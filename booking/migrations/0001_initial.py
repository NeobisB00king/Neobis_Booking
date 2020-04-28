# Generated by Django 2.2.8 on 2020-04-28 13:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookPayStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Статус оплаты')),
            ],
            options={
                'verbose_name': 'Статус оплаты',
                'verbose_name_plural': 'Статусы оплаты',
            },
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Статус брони')),
            ],
            options={
                'verbose_name': 'Статус комнаты',
                'verbose_name_plural': 'Статусы комнаты',
            },
        ),
        migrations.CreateModel(
            name='CategoryRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория комнаты',
                'verbose_name_plural': 'Категории комнат',
            },
        ),
        migrations.CreateModel(
            name='VolumeRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_name', models.CharField(max_length=64, verbose_name='Вместительность комнаты')),
            ],
            options={
                'verbose_name': 'Вместительность комнаты',
                'verbose_name_plural': 'Вместительность комнат',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название комнаты')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('images', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Вместительность категории')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_category', to='booking.CategoryRoom', verbose_name='Название категории')),
                ('volume', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_volume', to='booking.VolumeRoom', verbose_name='Вместительность категории')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(verbose_name='Бронировать с')),
                ('date_to', models.DateField(verbose_name='Бронировать до')),
                ('comment', models.CharField(blank=True, max_length=170, verbose_name='Комментарий')),
                ('book_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания брони')),
                ('has_child', models.BooleanField(blank=True, default=False, verbose_name='Есть ли ребенок')),
                ('clientName', models.CharField(max_length=64, verbose_name='Имя клиента')),
                ('clientSurname', models.CharField(max_length=64, verbose_name='Фамилия клиента')),
                ('clientEmail', models.EmailField(max_length=254, verbose_name='Email клиента')),
                ('clientPhone', models.IntegerField(verbose_name='Номер телефона клиента')),
                ('totalsum', models.IntegerField(default=0, verbose_name='Полная стоимость')),
                ('room_category_stats', models.CharField(blank=True, default='', max_length=64, verbose_name='Категория комнаты для статистики')),
                ('date_mass', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True, default=None, null=True, verbose_name='Даты'), blank=True, default=list, size=None)),
                ('book_pay_status', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='booking.BookPayStatus', verbose_name='Статус оплаты')),
                ('book_status', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='booking.BookStatus', verbose_name='Статус брони')),
                ('room', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='booking.Room', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
        migrations.CreateModel(
            name='BookSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Статистика брони',
                'verbose_name_plural': 'Статистка бронирования',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('booking.booking',),
        ),
    ]
