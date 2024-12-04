from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

user_model = get_user_model()

class EngineerProfile(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        related_name='engineer_profile'
    )
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  # Formato: xxx.xxx.xxx-xx
    crea = models.CharField(max_length=15, unique=True)  # Formato: x.xxx.xx-x
    funcao = models.CharField(max_length=50, blank=True, null=True)
    especializacao = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)  # Formato: (xx) xxxxx-xxxx
    ativo = models.BooleanField(default=True)
    cep = models.CharField(max_length=9)  # Formato: xxxxx-xxx
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.user.username})"

