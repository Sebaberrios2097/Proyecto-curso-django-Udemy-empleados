# Generated by Django 4.2 on 2023-04-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_prueba_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cantidad'),
        ),
    ]
