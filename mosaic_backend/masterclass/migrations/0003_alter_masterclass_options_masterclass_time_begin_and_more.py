# Generated by Django 4.1.6 on 2023-02-25 09:43

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0002_alter_masterclass_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='masterclass',
            options={'ordering': ['-time_begin'], 'verbose_name': 'Masterclass', 'verbose_name_plural': 'Masterclasses'},
        ),
        migrations.AddField(
            model_name='masterclass',
            name='time_begin',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 9, 43, 25, 677295)),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 9, 43, 25, 677304)),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Тип мастеркласса'),
        ),
    ]
