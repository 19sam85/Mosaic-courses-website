# Generated by Django 4.1.6 on 2023-02-25 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0005_alter_masterclass_time_begin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masterclasses', to='masterclass.masterclasstype', verbose_name='Выбор из предзаведенныхтипов мастерклассов'),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='currency',
            field=models.CharField(choices=[('тенге', 'тенге'), ('руб.', 'руб.'), ('eur', 'eur')], default='тенге', max_length=20),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
