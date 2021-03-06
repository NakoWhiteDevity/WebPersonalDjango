# Generated by Django 3.0.8 on 2020-07-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosDeInteres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato', models.CharField(max_length=50, verbose_name='Dato de interes')),
            ],
            options={
                'verbose_name': 'dato de interes',
                'verbose_name_plural': 'datos de interes',
                'ordering': ['dato'],
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=50, verbose_name='Puesto de trabajo')),
                ('ano', models.DateField(verbose_name='Año')),
                ('duracion', models.CharField(max_length=20, verbose_name='Duración')),
                ('lugar', models.CharField(max_length=50, verbose_name='Lugar')),
                ('tareas', models.TextField(max_length=600, verbose_name='Descripción y tareas')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'experiencia',
                'verbose_name_plural': 'experiencias',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacion', models.CharField(max_length=50, verbose_name='Formación recibida')),
                ('ano', models.CharField(max_length=10, verbose_name='año/s de realización')),
                ('lugar', models.CharField(max_length=50, verbose_name='Lugar de realización')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'formacion',
                'verbose_name_plural': 'formaciones',
                'ordering': ['-creado'],
            },
        ),
    ]
