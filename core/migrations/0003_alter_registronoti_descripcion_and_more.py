# Generated by Django 4.1.2 on 2024-06-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_descripcion_registronoti_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registronoti',
            name='descripcion',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='registronoti',
            name='link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registronoti',
            name='reportero',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registronoti',
            name='subtitulo',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registronoti',
            name='titulo',
            field=models.CharField(max_length=1000),
        ),
    ]