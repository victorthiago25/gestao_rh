# Generated by Django 2.1 on 2019-07-29 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190729_0426'),
        ('registro_hora_extra', '0002_auto_20190729_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_hora_extra',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]