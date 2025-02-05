# Generated by Django 5.0.6 on 2024-06-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('idade', models.IntegerField()),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('time', models.CharField(max_length=100)),
                ('posicao', models.CharField(max_length=20)),
            ],
        ),
    ]
