# Generated by Django 5.1 on 2024-08-21 20:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_alter_jogos_média_horas_jogando'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('chave_imagem', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('imagem', models.ImageField(upload_to='ProjetoDjangoREST//API//api//Imagens')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='API.jogos')),
            ],
        ),
    ]
