# Generated by Django 3.0.1 on 2019-12-22 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogador',
            name='clubeAtual',
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='nome',
        ),
    ]