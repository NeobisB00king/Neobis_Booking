# Generated by Django 3.0.4 on 2020-04-11 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryroom',
            options={'verbose_name': 'Категория комнаты', 'verbose_name_plural': 'Категории комнат'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterModelOptions(
            name='volumeroom',
            options={'verbose_name': 'Вместительность комнаты', 'verbose_name_plural': 'Вместительность комнат'},
        ),
        migrations.RemoveField(
            model_name='room',
            name='capacity',
        ),
        migrations.AlterField(
            model_name='categoryroom',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_category', to='booking.CategoryRoom', verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='room',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Вместительность категории'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название комнаты'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='room',
            name='volume',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_volume', to='booking.VolumeRoom', verbose_name='Вместительность категории'),
        ),
        migrations.AlterField(
            model_name='volumeroom',
            name='volume_name',
            field=models.CharField(max_length=64, verbose_name='Вместительность комнаты'),
        ),
    ]
