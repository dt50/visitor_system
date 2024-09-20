# Generated by Django 5.0.1 on 2024-09-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visits", "0006_visits_visits_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompletedSession",
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
                    "create",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp of object create",
                        verbose_name="Create time",
                    ),
                ),
                (
                    "update",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Timestamp of object update",
                        verbose_name="Update time",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("held", "Held"), ("not_held", "Not held")],
                        default="not_held",
                        max_length=255,
                        verbose_name="Session status",
                    ),
                ),
                ("reason", models.TextField(verbose_name="Session reason")),
            ],
            options={
                "verbose_name": "Completed session",
                "verbose_name_plural": "Completed sessions",
                "db_table": "completed_session",
                "db_table_comment": "Table include data of all completed sessions",
                "ordering": ("update",),
                "get_latest_by": "update",
            },
        ),
        migrations.AddField(
            model_name="visits",
            name="completed_sessions",
            field=models.ManyToManyField(
                blank=True,
                to="visits.completedsession",
                verbose_name="Completed sessions",
            ),
        ),
    ]
