# Generated by Django 5.0.9 on 2024-10-16 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0002_player_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="Position",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="player",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="player",
            name="age",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="player",
            name="position",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="players.position"
            ),
        ),
    ]
