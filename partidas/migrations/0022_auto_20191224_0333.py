# Generated by Django 3.0.1 on 2019-12-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gols', '0007_remove_gol_partida'),
        ('partidas', '0021_auto_20191224_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='gols',
            field=models.ManyToManyField(blank=True, max_length=2, to='gols.Gol'),
        ),
    ]
