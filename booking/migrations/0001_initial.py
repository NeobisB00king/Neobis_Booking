# Generated by Django 3.0.3 on 2020-02-08 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название категории')),
                ('volume', models.CharField(max_length=20, verbose_name='Вместительность')),
                ('special', models.TextField(verbose_name='Дополнительная информация')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Номер брони')),
                ('client_name', models.CharField(max_length=50, verbose_name='Клиент')),
                ('client_email', models.EmailField(max_length=100, verbose_name='Электронная почта клиента')),
                ('time_from', models.DateField(verbose_name='Время заезда')),
                ('time_to', models.DateField(verbose_name='Время выезда')),
                ('sum_price', models.ImageField(upload_to='', verbose_name='Сумма')),
                ('status_pay', models.CharField(choices=[('P', 'Paid'), ('UN', 'Unpaid')], default='UN', max_length=10)),
                ('special_request', models.TextField(verbose_name='Возможные пожелания')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Номер комнаты')),
                ('photos', models.ImageField(upload_to='', verbose_name='Фото')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.CategoryRoom', verbose_name='Тип номера')),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.Reservation', verbose_name='Бронь')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
    ]