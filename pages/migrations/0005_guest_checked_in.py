# Generated by Django 3.1.2 on 2020-11-11 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201106_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='checked_in',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]