
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Obra
from .forms import ObraForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_obras(request):
    obras = Obra.objects.filter(ativo=True)
    return render(request, 'obras/listar.html', {'obras': obras})

@login_required
def criar_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('obras:listar_obras'))
    else:
        form = ObraForm()
    return render(request, 'obras/form.html', {'form': form})

@login_required
def editar_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    if request.method == 'POST':
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect(reverse('obras:listar_obras'))
    else:
        form = ObraForm(instance=obra)
    return render(request, 'obras/form.html', {'form': form})

@login_required
def excluir_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    if request.method == 'POST':
        obra.delete()
        return redirect(reverse('obras:listar_obras'))
    return render(request, 'obras/confirmar_exclusao.html', {'obra': obra})

# View necessária para o CEP

from django.http import JsonResponse
import requests

def buscar_cep(request):
    cep = request.GET.get('cep', '').replace('-', '')  # Remove o hífen
    if not cep.isdigit() or len(cep) != 8:
        return JsonResponse({'erro': 'CEP inválido'}, status=400)

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'erro' in data:
            return JsonResponse({'erro': 'CEP não encontrado'}, status=404)
        return JsonResponse(data)  # Retorna os dados do ViaCEP
    return JsonResponse({'erro': 'Erro ao consultar o serviço de CEP'}, status=500)

