# Generated by Django 3.0.1 on 2019-12-23 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rodadas', '0004_auto_20191223_0248'),
        ('partidas', '0007_partida_temporada'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='rodada',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rodadas.Rodada'),
        ),
    ]
