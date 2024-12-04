from django import forms
from .models import Obra
import re
import requests  # Para buscar o CEP
from users.models import EngineerProfile

enginnerModel = EngineerProfile

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'
        widgets = {
            'cep': forms.TextInput(attrs={'id': 'cep-input', 'placeholder': 'Digite o CEP'}),
            'logradouro': forms.TextInput(attrs={'id': 'id_logradouro'}),
            'bairro': forms.TextInput(attrs={'id': 'id_bairro'}),
            'municipio': forms.TextInput(attrs={'id': 'id_municipio'}),
            'estado': forms.TextInput(attrs={'id': 'id_estado'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Popula o campo de engenheiro com engenheiros ativos
        self.fields['engenheiro_responsavel'].queryset = enginnerModel.objects.filter(ativo=True)

    def clean_cep(self):
        """
        Valida e formata o campo de CEP.
        Aceita entrada no formato XXXXX-XXX ou XXXXXXXX.
        Remove caracteres não numéricos e retorna no formato padrão XXXXX-XXX.
        """
        cep = self.cleaned_data['cep']
        cep = re.sub(r'[^0-9]', '', cep)  # Remove traços e outros caracteres não numéricos
        if not re.match(r'^\d{8}$', cep):  # Confirma que o CEP tem exatamente 8 dígitos
            raise forms.ValidationError("CEP inválido! Formato esperado: XXXXX-XXX ou XXXXXXXX")
        return f"{cep[:5]}-{cep[5:]}"  # Retorna no formato XXXXX-XXX

    def clean(self):
        cleaned_data = super().clean()
        cep = cleaned_data.get('cep')

        # Consulta API para buscar endereço
        if cep:
            response = requests.get(f"https://viacep.com.br/ws/{cep.replace('-', '')}/json/")
            if response.status_code == 200:
                data = response.json()
                if 'erro' not in data:
                    cleaned_data['logradouro'] = data.get('logradouro')
                    cleaned_data['bairro'] = data.get('bairro')
                    cleaned_data['municipio'] = data.get('localidade')
                    cleaned_data['estado'] = data.get('uf')
                else:
                    self.add_error('cep', 'CEP não encontrado.')
            else:
                self.add_error('cep', 'Erro ao consultar o serviço de CEP.')
        return cleaned_data
