# Generated by Django 4.2 on 2023-04-21 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_alter_departamento_anulate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], default='0', max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]