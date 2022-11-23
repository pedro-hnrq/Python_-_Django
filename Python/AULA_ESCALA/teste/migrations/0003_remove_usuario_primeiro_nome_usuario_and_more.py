# Generated by Django 4.1.3 on 2022-11-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_usuario_primeiro_nome_usuario'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='usuario',
            name='primeiro_nome_usuario',
        ),
        migrations.AddIndex(
            model_name='usuario',
            index=models.Index(fields=['primeiro_nome'], name='primeiro_nome_usuario'),
        ),
        migrations.AddIndex(
            model_name='usuario',
            index=models.Index(fields=['ultimo_nome'], name='ultimo_nome_usuario'),
        ),
    ]
