# Generated by Django 2.2.8 on 2020-04-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20200418_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_category_stats',
            field=models.CharField(default='', max_length=64, verbose_name='Категория комнаты для статистики'),
        ),
    ]