# Generated by Django 4.1.6 on 2023-06-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_alter_artworkmainpage_artwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='author_type',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], max_length=15),
        ),
    ]
