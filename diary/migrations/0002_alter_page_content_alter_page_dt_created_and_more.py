# Generated by Django 4.0.1 on 2022-01-25 05:07

import diary.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(validators=[diary.validators.validate_no_hash]),
        ),
        migrations.AlterField(
            model_name='page',
            name='dt_created',
            field=models.DateField(verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='page',
            name='feeling',
            field=models.CharField(max_length=80, validators=[diary.validators.validate_no_numbers]),
        ),
        migrations.AlterField(
            model_name='page',
            name='score',
            field=models.IntegerField(validators=[diary.validators.validate_score]),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100, validators=[diary.validators.validate_no_hash]),
        ),
    ]