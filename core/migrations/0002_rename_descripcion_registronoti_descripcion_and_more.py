# Generated by Django 4.1.2 on 2024-06-25 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registronoti',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='registronoti',
            name='fecha',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
