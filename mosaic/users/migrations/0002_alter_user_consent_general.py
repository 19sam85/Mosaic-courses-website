# Generated by Django 3.2.16 on 2022-11-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='consent_general',
            field=models.BooleanField(blank=True),
        ),
    ]
