# Generated by Django 3.0.1 on 2019-12-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubes', '0006_auto_20191222_2135'),
        ('partidas', '0005_auto_20191223_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='clubes',
            field=models.ManyToManyField(max_length=2, to='clubes.Clube'),
        ),
    ]
