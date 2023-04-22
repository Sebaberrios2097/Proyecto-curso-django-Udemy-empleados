# Generated by Django 4.2 on 2023-04-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('shor_name', models.CharField(max_length=20, verbose_name='Nombre corto')),
                ('anulate', models.BooleanField(default=True, verbose_name='Anulado')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['name'],
                'unique_together': {('name', 'shor_name')},
            },
        ),
    ]
