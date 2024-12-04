


import requests
from django.db import models
from django.contrib.auth import get_user_model
from users.models import EngineerProfile

engineerModel = EngineerProfile

class Obra(models.Model):
    nome = models.CharField(max_length=200)
    engenheiro_responsavel = models.ForeignKey(engineerModel, on_delete=models.CASCADE, related_name="obras")
    ativo = models.BooleanField(default=True)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)  
    data_modificacao = models.DateTimeField(auto_now=True)  

    def consultar_cep(self):
        """
        Consulta a API do ViaCEP para preencher os campos baseados no CEP.
        """
        if self.cep:
            try:
                cep_num = self.cep.replace('-', '')  # Remove o hífen para a API
                url = f'https://viacep.com.br/ws/{cep_num}/json/'
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    if not data.get('erro'):  # Verifica se a resposta é válida
                        self.logradouro = data.get('logradouro', '')
                        self.bairro = data.get('bairro', '')
                        self.municipio = data.get('localidade', '')
                        self.estado = data.get('uf', '')
            except Exception as e:
                print(f"Erro ao consultar CEP: {e}")

    def save(self, *args, **kwargs):
        # Realiza a consulta ao CEP antes de salvar
        self.consultar_cep()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

