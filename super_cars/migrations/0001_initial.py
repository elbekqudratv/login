# Generated by Django 5.0.2 on 2024-03-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "car_name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Car name"
                    ),
                ),
                ("car_desc", models.TextField(verbose_name="car characteristics")),
                (
                    "car_image",
                    models.ImageField(
                        upload_to="images/cars/", verbose_name="Car image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Cars",
                "verbose_name_plural": "Cars",
                "db_table": "cars",
                "ordering": ["id"],
            },
        ),
    ]
