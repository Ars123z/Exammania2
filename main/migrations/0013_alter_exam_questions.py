# Generated by Django 4.2.5 on 2023-11-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_alter_exam_questions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="questions",
            field=models.ManyToManyField(
                blank=True, related_name="Exams", to="main.examquestion"
            ),
        ),
    ]
