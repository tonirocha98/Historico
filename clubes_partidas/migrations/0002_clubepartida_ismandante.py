# Generated by Django 3.0.1 on 2019-12-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubes_partidas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubepartida',
            name='isMandante',
            field=models.BooleanField(default=True),
        ),
    ]
