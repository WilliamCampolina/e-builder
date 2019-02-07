# Generated by Django 2.1.3 on 2018-12-03 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descricao', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoConta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('deb_cred', models.CharField(max_length=1, verbose_name='Débito ou Crédito')),
            ],
        ),
        migrations.AddField(
            model_name='conta',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.TipoConta'),
        ),
    ]