# Generated by Django 3.0.1 on 2019-12-23 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0007_auto_20191222_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='altura',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
