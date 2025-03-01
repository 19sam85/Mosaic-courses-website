# Generated by Django 4.1.6 on 2023-02-25 10:19

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0006_alter_masterclass_course_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterclass',
            name='address',
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masterclasses', to='masterclass.masterclasstype', verbose_name='Выбор типа курса из предустановленных вариантов'),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, "Price can't be negative")]),
        ),
    ]
