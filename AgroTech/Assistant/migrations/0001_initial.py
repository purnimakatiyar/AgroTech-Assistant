# Generated by Django 4.1.7 on 2023-04-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sgn",
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
                ("username", models.CharField(max_length=122)),
                ("fname", models.CharField(max_length=122)),
                ("lname", models.CharField(max_length=122)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="SupplierOrder",
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
                ("name", models.CharField(max_length=122)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("crop_name", models.CharField(max_length=122)),
                ("crop_quantity", models.CharField(max_length=122)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=122)),
                ("state", models.CharField(max_length=122)),
                ("zip", models.CharField(max_length=122)),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Suppsgn",
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
                ("username", models.CharField(max_length=122)),
                ("fname", models.CharField(max_length=122)),
                ("lname", models.CharField(max_length=122)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("address", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
    ]