# Generated by Django 4.2.2 on 2023-06-30 23:15

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Memory",
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
                ("title", models.CharField(max_length=64)),
                ("comment", models.TextField(blank=True, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                (
                    "certificate",
                    models.ImageField(
                        null=True, upload_to=polls.models.upload_certificate
                    ),
                ),
            ],
        ),
    ]