# Generated by Django 5.0.1 on 2024-09-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visits", "0005_visits_session_visits_type_visit"),
    ]

    operations = [
        migrations.AddField(
            model_name="visits",
            name="visits_count",
            field=models.PositiveSmallIntegerField(
                default=1, verbose_name="Visits count"
            ),
        ),
    ]
