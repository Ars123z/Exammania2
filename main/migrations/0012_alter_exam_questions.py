# Generated by Django 4.2.5 on 2023-11-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_book_chapter_exercise_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="questions",
            field=models.ManyToManyField(
                null=True, related_name="Exams", to="main.examquestion"
            ),
        ),
    ]
