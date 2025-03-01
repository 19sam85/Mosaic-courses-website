# Generated by Django 4.1.6 on 2023-08-02 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("masterclass", "0010_masterclasstype_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="masterclass",
            name="course_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="masterclasses",
                to="masterclass.masterclasstype",
                verbose_name="Basic course type",
            ),
        ),
    ]
