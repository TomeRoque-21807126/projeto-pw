# Generated by Django 4.0.4 on 2022-06-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_portfolio_concluido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('pontuacao', models.IntegerField(max_length=10)),
            ],
        ),
    ]
