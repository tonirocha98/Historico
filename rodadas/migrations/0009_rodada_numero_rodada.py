# Generated by Django 3.0.1 on 2019-12-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rodadas', '0008_auto_20191223_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='rodada',
            name='numero_rodada',
            field=models.IntegerField(default=0),
        ),
    ]
