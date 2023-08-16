# Generated by Django 4.1.6 on 2023-08-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("masterclass", "0013_alter_masterclass_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="masterclasstype",
            name="type",
        ),
        migrations.AddField(
            model_name="masterclasstype",
            name="title",
            field=models.CharField(
                default="testtitle", max_length=50, verbose_name="Title"
            ),
            preserve_default=False,
        ),
    ]
