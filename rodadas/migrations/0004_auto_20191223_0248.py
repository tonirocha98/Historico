# Generated by Django 3.0.1 on 2019-12-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rodadas', '0003_auto_20191223_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodada',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]