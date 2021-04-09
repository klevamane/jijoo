# Generated by Django 3.2 on 2021-04-09 09:04

from django.db import migrations, models

import jijoo.utils


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0005_item_is_sold"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="interest",
            name="user",
        ),
        migrations.AddField(
            model_name="interest",
            name="email",
            field=models.EmailField(default="onengiye@gmail.com", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="interest",
            name="location",
            field=models.CharField(default="ph", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="interest",
            name="mobile",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[jijoo.utils.validate_ng_mobile_number],
            ),
        ),
        migrations.AddField(
            model_name="interest",
            name="name",
            field=models.CharField(default="name", max_length=100),
            preserve_default=False,
        ),
    ]