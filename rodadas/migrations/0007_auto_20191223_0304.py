# Generated by Django 3.0.1 on 2019-12-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rodadas', '0006_auto_20191223_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodada',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]