# Generated by Django 4.1.3 on 2022-11-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=30)),
                ('ultimo_nome', models.CharField(max_length=30)),
                ('nota1', models.IntegerField()),
                ('nota2', models.IntegerField()),
            ],
        ),
    ]