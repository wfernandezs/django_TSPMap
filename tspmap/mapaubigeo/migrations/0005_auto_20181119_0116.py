# Generated by Django 2.1.1 on 2018-11-19 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapaubigeo', '0004_tipocentropoblado_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centropoblado',
            name='tipo',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='TipoCentroPoblado',
        ),
    ]
