# Generated by Django 3.1 on 2024-11-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=50)),
                ('año_lanzamiento', models.PositiveIntegerField()),
                ('frecuencia_base', models.FloatField(help_text='Frecuencia base en GHz')),
                ('frecuencia_maxima', models.FloatField(help_text='Frecuencia máxima en GHz')),
                ('numero_nucleos', models.PositiveIntegerField()),
                ('numero_hilos', models.PositiveIntegerField()),
                ('cache_L3', models.FloatField(help_text='Tamaño de la caché L3 en MB')),
                ('tdp', models.FloatField(help_text='TDP en vatios')),
                ('arquitectura', models.CharField(max_length=50)),
                ('tecnologia_fabricacion', models.FloatField(help_text='Tecnología de fabricación en nm')),
                ('soporte_multithreading', models.BooleanField(default=False)),
                ('precio_lanzamiento', models.FloatField(help_text='Precio de lanzamiento en USD')),
            ],
            options={
                'verbose_name': 'Procesador',
                'verbose_name_plural': 'Procesadores',
                'ordering': ['año_lanzamiento'],
            },
        ),
    ]