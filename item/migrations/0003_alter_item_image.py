# Generated by Django 3.2 on 2021-04-08 22:58

from django.db import migrations, models

import item.models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0002_auto_20210408_2215"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=item.models.upload_image
            ),
        ),
    ]
