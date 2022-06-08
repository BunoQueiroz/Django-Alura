# Generated by Django 4.0.4 on 2022-06-08 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_alter_pessoa_cargo'),
        ('pratos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
    ]
