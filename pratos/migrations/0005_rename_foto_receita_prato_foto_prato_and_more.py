# Generated by Django 4.0.4 on 2022-06-09 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratos', '0004_prato_data_criacao_prato_foto_receita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prato',
            old_name='foto_receita',
            new_name='foto_prato',
        ),
        migrations.AlterField(
            model_name='prato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 8, 48, 10, 180083)),
        ),
    ]
