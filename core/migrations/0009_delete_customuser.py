# Generated by Django 4.1.2 on 2024-06-29 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_customuser_apellido_customuser_correo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]