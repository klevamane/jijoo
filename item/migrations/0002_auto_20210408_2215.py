# Generated by Django 3.2 on 2021-04-08 22:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="descriprion",
            new_name="description",
        ),
        migrations.AlterField(
            model_name="item",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
