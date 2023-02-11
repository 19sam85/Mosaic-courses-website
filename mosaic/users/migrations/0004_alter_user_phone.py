# Generated by Django 4.1.6 on 2023-02-11 04:33

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
    ]
