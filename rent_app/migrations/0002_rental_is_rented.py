# Generated by Django 2.2.4 on 2020-12-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
    ]