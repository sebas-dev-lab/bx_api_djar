# Generated by Django 3.2.6 on 2022-05-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bxlanding', '0004_presentationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentationmodel',
            name='showLatitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='presentationmodel',
            name='showLongitude',
            field=models.FloatField(),
        ),
    ]