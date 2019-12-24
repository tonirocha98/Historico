# Generated by Django 3.0.1 on 2019-12-23 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temporadas', '0002_remove_temporada_melhor_jogador'),
        ('rodadas', '0010_auto_20191223_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodada',
            name='numero_rodada',
            field=models.IntegerField(default=0, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='rodada',
            name='temporada',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='temporadas.Temporada'),
        ),
    ]