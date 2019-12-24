# Generated by Django 3.0.1 on 2019-12-23 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clube_visitante', '0002_remove_clubevisitante_partida'),
        ('clube_mandante', '0002_remove_clubemandante_partida'),
        ('partidas', '0011_partida_clubes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='clubes',
        ),
        migrations.AddField(
            model_name='partida',
            name='clube_mandante',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='clube_mandante.ClubeMandante'),
        ),
        migrations.AddField(
            model_name='partida',
            name='clube_visitante',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='clube_visitante.ClubeVisitante'),
        ),
    ]