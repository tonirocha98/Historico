# Generated by Django 2.2.1 on 2019-05-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gols', '0002_gol_jogador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gol',
            name='jogador',
        ),
    ]
