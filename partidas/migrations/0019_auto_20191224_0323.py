# Generated by Django 3.0.1 on 2019-12-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0018_auto_20191224_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='publico',
            field=models.IntegerField(blank=True),
        ),
    ]