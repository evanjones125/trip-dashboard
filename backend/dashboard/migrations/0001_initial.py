# Generated by Django 4.1.7 on 2023-04-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("lat", models.DecimalField(decimal_places=6, max_digits=8)),
                ("trip_date", models.DateField()),
            ],
        ),
    ]
