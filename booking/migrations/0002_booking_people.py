# Generated by Django 3.2 on 2022-02-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='people',
            field=models.IntegerField(default=2),
        ),
    ]
