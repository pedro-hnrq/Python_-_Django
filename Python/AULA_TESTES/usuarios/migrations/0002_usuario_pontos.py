# Generated by Django 4.1.3 on 2022-11-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='pontos',
            field=models.IntegerField(default=0),
        ),
    ]
