# Generated by Django 2.2.8 on 2020-04-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_booking_room_category_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_category_stats',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Категория комнаты для статистики'),
        ),
    ]