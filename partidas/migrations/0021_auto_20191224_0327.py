# Generated by Django 3.0.1 on 2019-12-24 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0018_remove_jogador_clubeatual'),
        ('gols', '0007_remove_gol_partida'),
        ('partidas', '0020_auto_20191224_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='gols',
            field=models.ManyToManyField(blank=True, max_length=2, null=True, to='gols.Gol'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='melhor_jogador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='jogadores.Jogador'),
        ),
    ]
