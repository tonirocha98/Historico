# Generated by Django 3.0.1 on 2019-12-23 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clube_mandante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubemandante',
            name='partida',
        ),
    ]
