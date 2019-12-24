# Generated by Django 3.0.1 on 2019-12-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jogadores', '0014_auto_20191223_0354'),
        ('partidas', '0011_partida_clubes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jogadores.Jogador')),
                ('partida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='partidas.Partida')),
            ],
        ),
    ]
