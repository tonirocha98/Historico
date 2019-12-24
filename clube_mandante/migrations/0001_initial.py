# Generated by Django 3.0.1 on 2019-12-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubes', '0006_auto_20191222_2135'),
        ('partidas', '0011_partida_clubes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubeMandante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clube', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='clubes.Clube')),
                ('partida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='partidas.Partida')),
            ],
        ),
    ]