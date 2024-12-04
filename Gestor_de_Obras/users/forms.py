from django import forms
from .models import EngineerProfile

class EngineerProfileForm(forms.ModelForm):
    class Meta:
        model = EngineerProfile
        fields = [
            'nome', 'cpf', 'crea', 'funcao', 'data_nascimento', 'telefone',
            'cep', 'bairro', 'cidade', 'uf', 'logradouro', 'numero',
            'complemento', 'especializacao'
        ]
        labels = {
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'crea': 'CREA',
            'funcao': 'Função',
            'data_nascimento': 'Data de Nascimento',
            'telefone': 'Telefone',
            'cep': 'CEP',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'uf': 'UF',
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'complemento': 'Complemento',
            'especializacao': 'Especialização',
        }