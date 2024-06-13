# Generated by Django 4.2.13 on 2024-06-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("gender", models.CharField(max_length=30)),
                ("salary", models.IntegerField(default=0)),
                ("years_exp", models.IntegerField(default=0)),
                ("company_size", models.IntegerField(default=0)),
                ("industry", models.CharField(max_length=30)),
                ("role", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
            ],
        ),
    ]