# Generated by Django 2.1 on 2019-07-29 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro_hora_extra',
            old_name='nome',
            new_name='motivo',
        ),
    ]
