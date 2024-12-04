# Generated by Django 5.1.3 on 2024-11-24 15:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('crea', models.CharField(max_length=15, unique=True)),
                ('funcao', models.CharField(blank=True, max_length=50, null=True)),
                ('especializacao', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=15)),
                ('ativo', models.BooleanField(default=True)),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='engineer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]