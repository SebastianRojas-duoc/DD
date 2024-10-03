# Generated by Django 4.1.2 on 2024-06-30 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_perfilusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='rut',
            field=models.CharField(max_length=10),
        ),
    ]
