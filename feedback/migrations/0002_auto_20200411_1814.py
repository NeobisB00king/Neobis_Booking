# Generated by Django 3.0.4 on 2020-04-11 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminemail',
            options={'verbose_name': 'Email админа', 'verbose_name_plural': "Email'ы админа"},
        ),
    ]
