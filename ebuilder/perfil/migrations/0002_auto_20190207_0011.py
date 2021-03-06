# Generated by Django 2.1.5 on 2019-02-07 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilempresa',
            name='sobrenome',
        ),
        migrations.RemoveField(
            model_name='perfilempresa',
            name='topico',
        ),
        migrations.RemoveField(
            model_name='perfilprofissional',
            name='subtopico',
        ),
        migrations.AddField(
            model_name='perfilempresa',
            name='razaoSocial',
            field=models.CharField(default=0, max_length=100, verbose_name='Razão Social'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfilempresa',
            name='topicos',
            field=models.ManyToManyField(to='perfil.Topicos'),
        ),
        migrations.AddField(
            model_name='perfilprofissional',
            name='servicos',
            field=models.ManyToManyField(to='perfil.SubTopicos'),
        ),
        migrations.AddField(
            model_name='subtopicos',
            name='subtopicos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.Topicos'),
        ),
        migrations.AlterField(
            model_name='perfilempresa',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome Fantasia'),
        ),
        migrations.AlterField(
            model_name='perfilprofissional',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='perfilprofissional',
            name='sobrenome',
            field=models.CharField(max_length=100, verbose_name='Sobrenome'),
        ),
    ]
