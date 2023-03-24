# Generated by Django 4.1.1 on 2022-09-18 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produtos.produto')),
            ],
        ),
    ]