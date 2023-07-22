# Generated by Django 4.1.6 on 2023-06-24 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='author_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=15),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(default=None, upload_to='artworks/'),
        ),
        migrations.CreateModel(
            name='ArtworkMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_ordering', models.PositiveSmallIntegerField()),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.artwork')),
            ],
        ),
    ]
