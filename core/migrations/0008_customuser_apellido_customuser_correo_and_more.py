# Generated by Django 4.1.2 on 2024-06-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_customuser_delete_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='apellido',
            field=models.CharField(default='Apellido', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='correo',
            field=models.CharField(default='correo@example.com', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nombre_usuario',
            field=models.CharField(default='nombre_usuario', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='direccion',
            field=models.CharField(default='Dirección', max_length=1000),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fecha_nacimiento',
            field=models.CharField(default='01-01-1970', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='genero',
            field=models.IntegerField(choices=[(1, 'masculino'), (2, 'femenino'), (3, 'otro')], default=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rut',
            field=models.CharField(default='12345678-9', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefono',
            field=models.CharField(default='123456789', max_length=100),
        ),
    ]
