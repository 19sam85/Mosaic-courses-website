# Generated by Django 4.1.6 on 2023-02-25 09:44

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0003_alter_masterclass_options_masterclass_time_begin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='time_begin',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 9, 44, 29, 496082, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 9, 44, 29, 496211, tzinfo=datetime.timezone.utc)),
        ),
    ]
