# Generated by Django 2.1.3 on 2019-02-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20190207_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilempresa',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='perfilprofissional',
            name='usuario',
        ),
        migrations.AddField(
            model_name='perfilempresa',
            name='id_user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfilprofissional',
            name='id_user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
