# Generated by Django 4.1.2 on 2024-06-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_registronoti_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=100000)),
            ],
        ),
    ]
