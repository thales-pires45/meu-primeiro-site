# Generated by Django 4.0.2 on 2022-02-12 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'permissions': (('pode_manipular_cliente', 'Manipula o cadastro de contas.'),),
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('produtora', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('pode_manipular_filme', 'Manipula o cadastro de filme.'),),
            },
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_locacao', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('contas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.cliente')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.filme')),
            ],),
        migrations.AlterModelOptions(
               name='cliente',
              options={'permissions': (('pode_manipular_cliente', 'Manipula o cadastro de cliente.'),)},
          ),
    ]
