# Generated by Django 4.0.2 on 2022-02-13 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locacao',
            old_name='contas',
            new_name='cliente',
        ),
    ]
