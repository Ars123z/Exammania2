# Generated by Django 4.2.5 on 2023-10-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_examquestionoptions_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="examquestion",
            name="difficulty_level",
            field=models.CharField(
                choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")],
                default=None,
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="examquestion",
            name="subject",
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name="examquestion",
            name="body",
            field=models.TextField(unique=True),
        ),
    ]
