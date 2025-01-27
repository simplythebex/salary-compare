# Generated by Django 4.2.13 on 2024-06-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salaries", "0003_user_education_level"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="age",
        ),
        migrations.RemoveField(
            model_name="user",
            name="company_size",
        ),
        migrations.RemoveField(
            model_name="user",
            name="education_level",
        ),
        migrations.RemoveField(
            model_name="user",
            name="email",
        ),
        migrations.RemoveField(
            model_name="user",
            name="industry",
        ),
        migrations.AlterField(
            model_name="user",
            name="salary",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="user",
            name="years_exp",
            field=models.CharField(max_length=30),
        ),
    ]
