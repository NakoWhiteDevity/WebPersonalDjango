# Generated by Django 3.0.8 on 2020-07-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='ano',
            field=models.IntegerField(verbose_name='Año'),
        ),
    ]