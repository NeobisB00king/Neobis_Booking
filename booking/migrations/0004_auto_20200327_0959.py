# Generated by Django 3.0.4 on 2020-03-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200327_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ManyToManyField(to='booking.Room'),
        ),
        migrations.RemoveField(
            model_name='room',
            name='category',
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ManyToManyField(related_name='room_category', to='booking.CategoryRoom'),
        ),
        migrations.RemoveField(
            model_name='room',
            name='images',
        ),
        migrations.AddField(
            model_name='room',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='booking.RoomImages'),
        ),
        migrations.RemoveField(
            model_name='room',
            name='volume',
        ),
        migrations.AddField(
            model_name='room',
            name='volume',
            field=models.ManyToManyField(related_name='room_volume', to='booking.VolumeRoom'),
        ),
    ]
