# Generated by Django 3.0.1 on 2019-12-23 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estadios', '0003_auto_20191222_2119'),
        ('clubes', '0005_clube_estadio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='estadio',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='estadios.Estadio'),
        ),
        migrations.AlterField(
            model_name='clube',
            name='nome',
            field=models.TextField(default=''),
        ),
    ]
