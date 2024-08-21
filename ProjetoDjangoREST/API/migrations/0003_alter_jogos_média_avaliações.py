# Generated by Django 5.1 on 2024-08-21 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_jogos_média_avaliações_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='Média_Avaliações',
            field=models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
