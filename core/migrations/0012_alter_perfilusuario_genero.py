# Generated by Django 4.1.2 on 2024-06-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_perfilusuario_genero_alter_perfilusuario_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='genero',
            field=models.CharField(choices=[('', 'Seleccione una opción'), ('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
    ]
