# Generated by Django 4.1.6 on 2023-06-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_alter_school_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=450),
        ),
    ]
