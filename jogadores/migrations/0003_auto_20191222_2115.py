# Generated by Django 3.0.1 on 2019-12-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0002_auto_20191222_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='altura',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jogador',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jogador',
            name='nome',
            field=models.TextField(default='erro'),
        ),
        migrations.AddField(
            model_name='jogador',
            name='peso',
            field=models.TextField(null=True),
        ),
    ]