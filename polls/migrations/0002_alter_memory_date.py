# Generated by Django 4.2.2 on 2023-07-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memory",
            name="date",
            field=models.DateTimeField(),
        ),
    ]