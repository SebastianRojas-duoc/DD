# Generated by Django 4.1.2 on 2024-06-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='mensaje',
            new_name='mensajes',
        ),
    ]
