# Generated by Django 3.0.1 on 2019-12-22 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0002_partida_rodada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='clubes',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='rodada',
        ),
    ]