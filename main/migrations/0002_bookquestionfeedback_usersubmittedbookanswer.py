# Generated by Django 4.2.5 on 2024-02-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookQuestionFeedback",
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
                ("feedback", models.TextField()),
                ("book", models.CharField(max_length=250)),
                ("chapter", models.CharField(max_length=250)),
                ("exercise", models.CharField(max_length=250)),
                ("no", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="UserSubmittedBookAnswer",
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
                ("answer", models.TextField()),
                ("book", models.CharField(max_length=250)),
                ("chapter", models.CharField(max_length=250)),
                ("exercise", models.CharField(max_length=250)),
                ("no", models.IntegerField()),
            ],
        ),
    ]
