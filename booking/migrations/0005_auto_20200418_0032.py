# Generated by Django 2.2.8 on 2020-04-17 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20200418_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booksummary',
            options={'verbose_name': 'Статистика брони', 'verbose_name_plural': 'Статистка бронирования'},
        ),
    ]
